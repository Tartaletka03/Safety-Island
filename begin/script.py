from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import secrets
import os
import hashlib


# Поиск файла

import os

def find_path(filename):
    current_dir = os.getcwd()
    check_verification_path = os.path.join(current_dir, "Safety-Island", "begin", "docs", filename)
    return check_verification_path


# XOR Шифрование при помощи hash & salt


def generate_salt(length=64):
    """Генерирует случайный набор байт для соли."""
    return secrets.token_bytes(64)

def encrypt_block(block, key, salt):
    """Шифрует блок данных с использованием XOR и побитовых операций."""
    key_hash = hashlib.sha512((key.encode() + salt)).digest()
    shuffled_key = bytearray([key_hash[i % len(key_hash)] for i in range(len(block))])
    return bytes([b ^ k for b, k in zip(block, shuffled_key)])

def decrypt_block(block, key, salt):
    """Расшифровывает блок данных."""
    key_hash = hashlib.sha512((key.encode() + salt)).digest()
    shuffled_key = bytearray([key_hash[i % len(key_hash)] for i in range(len(block))])
    return bytes([b ^ k for b, k in zip(block, shuffled_key)]) 

def encrypt_file(key):
    """Шифрует файл с использованием блочной системы шифрования."""
    salt = generate_salt()

    with open(find_path("data.txt"), 'rb') as f:
        data = f.read()

    encrypted_data = bytearray()
    padding_length = 16 - (len(data) % 16)
    if padding_length > 0: data += bytes([padding_length]) * padding_length

    for i in range(0, len(data), 16):
        block = data[i:i + 16]
        encrypted_data.extend(encrypt_block(block, key, salt))

    with open(find_path("data.txt"), 'wb') as f:
        f.write(salt)
        f.write(encrypted_data)

def decrypt_file(key):
    """Расшифровывает файл с использованием блочной системы шифрования."""

    with open(find_path("data.txt"), 'rb') as f:
        salt = f.read(64)
        encrypted_data = f.read()

    decrypted_data = bytearray()
    for i in range(0, len(encrypted_data), 16):
        block = encrypted_data[i:i + 16]
        decrypted_data.extend(decrypt_block(block, key, salt))

    padding_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding_length]

    with open(find_path("data.txt"), 'wb') as f:
        f.write(decrypted_data)


# Шифрование при помощи Fernet & hash


def generate_key_from_password(password):
    """Генерирует ключ Fernet на основе пароля и соли."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=32,
        salt=b"The party will not forget you, comrades.",
        iterations=20000,
        backend=default_backend()
    )
    
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def fernet_encrypt_file(key):
    """Шифрует файл с помощью ключа Fernet."""
    f = Fernet(key)

    filename = find_path("data.txt")

    with open(filename, 'rb') as file:
        original_data = file.read()

    encrypted_data = f.encrypt(original_data)

    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def fernet_decrypt_file(key):
    """Расшифровывает файл с помощью ключа Fernet."""
    f = Fernet(key)

    with open(find_path("data.txt"), 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(find_path("data.txt"), 'wb') as file:
        file.write(decrypted_data)

def update_state(filename, state):
    with open(filename, "w") as file:
        file.write(state)


# Логика


def change_password():
    """Логика смены пароля."""
    while True:
        new_password = input("Введите новый пароль: ")
        confirm_password = input("Введите пароль еще раз: ")

        if new_password == confirm_password:
            hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
            with open(find_path("check_verification.txt"), "w") as file:
                file.write(hashed_new_password)
            print("Пароль успешно изменен!")
            break
        else:
            print("Пароли не совпадают. Попробуйте снова.")

def generate_password(length=24, 
                               uppercase=True, 
                               lowercase=True, 
                               digits=True, 
                               symbols=True):
    """
    Генерирует и возвращает хэш надежного пароля.
    """

    characters = ''
    if uppercase: characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if lowercase: characters += 'abcdefghijklmnopqrstuvwxyz'
    if digits: characters += '0123456789'
    if symbols: characters += '!@#$%^&*()_+-=[]{};\':"\\|,.<>/?~'

    return ''.join(secrets.choice(characters) for _ in range(length))



"""

Функции для взаимодействия с оболочкой


"""


def TFpassword(): # Проверка существования файла и наличия текста в нем
    try:

        with open(find_path("check_vertification.txt"), "r") as file: # Читаем содержимое файла
            file_content = file.read().strip()  # Удаляем пробельные символы с начала и конца строки
            hachPassword = bool(file_content)  # Флаг, указывающий на наличие пароля

    except FileNotFoundError: hachPassword = False  # Флаг, указывающий на отсутствие пароля
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        hachPassword = False

    return hachPassword

def hidden_password(password): # Функция проверяет, сравнивает пароль, либо вносит новый в файл
    if TFpassword():
        with open(find_path("check_vertification.txt"), "r") as file: # Читаем содержимое файла
            file_content = file.read().strip()

        
        hashed_input = hashlib.sha256(password.encode()).hexdigest() # Хеширование введенного пароля 
        if hashed_input == file_content: # Сравнение хешей
            return True 

        else:
            return False
        
    else: 
        # Хеширование пароля
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Запись хешированного пароля в файл
        with open(find_path("check_vertification.txt"), "w") as file:
            file.write(hashed_password)
        return True


def enc(password): # Вызов функции шифрует файл data
    if TFpassword():
        with open(find_path("check_vertification.txt"), "r") as file: # Читаем содержимое файла
            file_content = file.read().strip()

        
        hashed_input = hashlib.sha256(password.encode()).hexdigest() # Хеширование введенного пароля 
        if hashed_input == file_content: # Сравнение хешей

            with open(find_path("state.txt"), "r") as file:
                state = file.read().strip()

            fernet_encrypt_file(generate_key_from_password(password))
            encrypt_file(hashlib.sha512(password.encode()).hexdigest())
            update_state(find_path("state.txt"), "decrypted")  # Обновляем состояние

def dec(password):
    if TFpassword():
        with open(find_path("check_vertification.txt"), "r") as file: # Читаем содержимое файла
            file_content = file.read().strip()

        
        hashed_input = hashlib.sha256(password.encode()).hexdigest() # Хеширование введенного пароля 
        if hashed_input == file_content: # Сравнение хешей

            with open(find_path("state.txt"), "r") as file:
                state = file.read().strip()

            if state == "decrypted": # Дешифровка
                decrypt_file(hashlib.sha512(password.encode()).hexdigest())
                fernet_decrypt_file(generate_key_from_password(password))
                update_state(find_path("state.txt"), "encrypted")  # Обновляем состояние
            else:
                return False



def change_password(new_password): # Функция заменяет пароль
    with open(find_path("check_vertification.txt"), "w") as file:
        file.write(hashlib.sha256(new_password.encode()).hexdigest())