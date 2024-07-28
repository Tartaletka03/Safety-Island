import hashlib
import secrets
import os


# Функции

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

def update_state(filename, state):
    with open(filename, "w") as file:
        file.write(state)



# Проверка существования файла и наличия текста в нем
try:

    with open("docs/check_vertification.txt", "r") as file:
        # Читаем содержимое файла
        file_content = file.read().strip()  # Удаляем пробельные символы с начала и конца строки
        hachPassword = bool(file_content)  # Флаг, указывающий на наличие пароля

except FileNotFoundError: hachPassword = False  # Флаг, указывающий на отсутствие пароля
except Exception as e:
    print(f"Ошибка при чтении файла: {e}")
    hachPassword = False


if hachPassword:
    while True:
        password = input("Введите пароль: ")
        # Хеширование введенного пароля
        hashed_input = hashlib.sha256(password.encode()).hexdigest()
        # Сравнение хешей
        if hashed_input == file_content:
            print("Доступ разрешен!")


            filename = "docs/data.txt"  # Имя файла, который нужно зашифровать/расшифровать

            # Процесс шифровки/дешифровки
            while True:
                with open("docs/state.txt", "r") as file:
                    state = file.read().strip()

                if state == "encrypted":
                    choice = input("Шифровать (Y)? ")
                    if choice.lower() == 'y':
                        encrypt_file(filename, password)
                        print(f"Файл {filename} зашифрован.")
                        password = None  # Обнуляем переменную с паролем
                        update_state("docs/state.txt", "decrypted")  # Обновляем состояние
                        break  # Выходим из цикла
                    else:
                        print("Некорректный выбор")
                elif state == "decrypted":
                    choice = input("Расшифровать (Y)? ")
                    if choice.lower() == 'y':
                        decrypt_file(filename, password)
                        print(f"Файл {filename} расшифрован.")
                        update_state("docs/state.txt", "encrypted")  # Обновляем состояние
                        break  # Выходим из цикла
                    else:
                        print("Некорректный выбор")
                else:
                    print("Некорректный выбор")


            password = None # Обнуляем переменную с паролем
            break
        else:
            print("Неверный пароль. Попробуйте снова.")

        password = None # Обнуляем переменную с паролем
else:
    # Создание нового пароля
    while True:
        password = input("Придумайте пароль не менее 12 символов: ")
        if len(password) >= 12:
            break
        else:
            print("Пароль должен быть не менее 12 символов.")

    # Хеширование пароля
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Запись хешированного пароля в файл
    try:
        with open("docs/check_vertification.txt", "w") as file:
            file.write(hashed_password)
        print("Пароль записан.")

        filename = "docs/data.txt"  # Имя файла, который нужно зашифровать/расшифровать

        # Процесс шифровки/дешифровки
        while True:
            choice = input("Шифровать (Y)? ")
        
            if choice.lower() == 'y':
                encrypt_file(filename, password)
                print(f"Файл {filename} зашифрован.")
                password = None # Обнуляем переменную с паролем
                with open("docs/state.txt", "w") as file:
                    file.write("decrypted")
                break
            else: print("Некорректный выбор")

    except Exception as e:
        print(f"Ошибка при записи пароля в файл: {e}")

    password = None # Обнуляем переменную с паролем