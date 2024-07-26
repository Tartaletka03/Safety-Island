import hashlib
import secrets

password = r"C:\Users\HP\Desktop\Managerpassword\KeeperC:\Users\HP\Desktop\C:\Users\HP\Desktop\>"  

def generate_salt(length=64):
    """Генерирует случайный набор байт для соли."""
    return secrets.token_bytes(64)

def encrypt_block(block, key, salt):
    """Шифрует блок данных с использованием XOR и побитовых операций."""
    key = hashlib.sha512((key.encode() + salt)).digest()  # SHA-512 хэш ключа с солью
    return bytes([b ^ k for b, k in zip(block, key)])

def decrypt_block(block, key, salt):
    """Расшифровывает блок данных."""
    return encrypt_block(block, key, salt)  # Дешифрование - это обратная операция шифрования

def encrypt_file(filename, key):
    """Шифрует файл с использованием блочной системы шифрования."""
    salt = generate_salt()  # Генерация соли для каждого файла


    with open(filename, 'rb') as f:
        data = f.read()

    encrypted_data = bytearray()
    padding_length = 16 - (len(data) % 16)  # Длина заполнения

    # Добавление заполнения 
    if padding_length > 0:
        data += bytes([padding_length]) * padding_length

    for i in range(0, len(data), 16):  # Обрабатываем файл блоками по 16 байт
        block = data[i:i + 16]
        encrypted_data.extend(encrypt_block(block, key, salt))

    # Сохраняем соль и зашифрованные данные
    with open(filename, 'wb') as f:
        f.write(salt)
        f.write(encrypted_data)

def decrypt_file(filename, key):
    """Расшифровывает файл с использованием блочной системы шифрования."""
    with open(filename, 'rb') as f:
        salt = f.read(64)  # Считываем соль с начала файла
        encrypted_data = f.read()

    decrypted_data = bytearray()
    for i in range(0, len(encrypted_data), 16):
        block = encrypted_data[i:i + 16]
        decrypted_data.extend(decrypt_block(block, key, salt))

    # Удаление заполнения
    padding_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding_length]

    with open(filename, 'wb') as f:
        f.write(decrypted_data)

if __name__ == "__main__":
    filename = "data.txt"  # Имя файла, который нужно зашифровать/расшифровать
    
    while True:
        choice = input("Шифровать (e) или расшифровать (d)? ")
        
        if choice.lower() == 'e':
            encrypt_file(filename, password)
            print(f"Файл {filename} зашифрован.")
            break
        elif choice.lower() == 'd':
            decrypt_file(filename, password)
            print(f"Файл {filename} расшифрован.")
            break
        else:
            print("Некорректный выбор. Введите 'e' или 'd'.")
