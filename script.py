import hashlib

hachPassword = False


if hachPassword:
    print("Текст уже есть в файле.")





else:
    while True:
        password = input("Придумайте пароль не менее 12 символов: ")
        if len(password) >= 12:
            break
        else:
            print("Пароль должен быть не менее 12 символов.")

    # Хеширование пароля
    password = hashlib.sha512(password.encode()).hexdigest()
    txt = "abra kadabra? sim salovim? SPASIBO!"

    # Запись хешированного пароля и текста в файл
    with open(filename, "w") as file:
        file.write(hashlib.sha512(txt.encode()).hexdigest())
    print("Пароль записан")
