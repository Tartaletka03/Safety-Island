from script import *
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import pyperclip

def create_new_passw_win():
    global new_passw_win, newPassw, alertMess1
    new_passw_win = Tk()
    new_passw_win.title('SafeNote')
    new_passw_win.geometry('300x250+400+400')
    new_passw_win.resizable(False, False)

    Label(text='Придумайте пароль:').pack(pady=20)
    newPassw = ttk.Entry(width=35)
    newPassw.pack(pady=10)
    alertMess1 = Label(text='')
    alertMess1.pack()
    Label().pack()
    svBtn = ttk.Button(text='Сохранить', command=click_svBtn_event)
    svBtn.pack(pady=30)

    new_passw_win.mainloop()

def create_veref_win():
    global veref_win, verefPassw, alertMess3
    veref_win = Tk()
    veref_win.title('SafeNote')
    veref_win.geometry('300x250+400+400')
    veref_win.resizable(False, False)

    Label(text='Введите пароль:').pack(pady=20)
    verefPassw = ttk.Entry(width=35)
    verefPassw.pack(pady=10)
    alertMess3 = Label(text='')
    alertMess3.pack()
    Label().pack()
    verefBtn = ttk.Button(text='Войти', command=click_verefBtn_event)
    verefBtn.pack(pady=30)

    veref_win.mainloop()

def create_note_win():
    global note_win, genOutput, editor, genBtn
    note_win = Tk()
    note_win.title("SafeNote")
    note_win.geometry("300x450+400+400")
    note_win.resizable(False, False)

    editor = ScrolledText()
    editor.pack()
    svBtn = ttk.Button(text='Сохранить')
    svBtn.place(x=20, y=392)
    genOutput = Label(text='', anchor='e', width=23)
    genOutput.place(x=108, y=393)
    chngPasswBtn = ttk.Button(text='Изменить пароль', command=click_chngPasswBtn_event)
    chngPasswBtn.place(x=20, y=420)
    genBtn = ttk.Button(text='Сгенерировать пароль', width=21, command=click_genBtn_event)
    genBtn.place(x=140, y=420)

    note_win.mainloop()

def create_chng_passw_win():
    global chng_passw_win, confPassw, chngPassw, alertMess2
    chng_passw_win = Tk()
    chng_passw_win.title('SafeNote')
    chng_passw_win.geometry('300x250+400+400')
    chng_passw_win.resizable(False, False)

    Label(text='Введите новый пароль:').pack(pady=10)
    chngPassw = ttk.Entry(width=35)
    chngPassw.pack()
    Label(text='Введите новый пароль ещё раз:').pack(pady=10)
    confPassw = ttk.Entry(width=35)
    confPassw.pack()
    alertMess2 = Label(text='')
    alertMess2.pack(pady=10)
    svChngBtn = ttk.Button(text='Сохранить', command=click_svChngBtn_event)
    svChngBtn.place(x=150, y=195)
    bckToNtBtn = ttk.Button(text='Вернуться', command=click_bckToNtBtn_event)
    bckToNtBtn.place(x=70, y=195)

    chng_passw_win.mainloop()

def click_genBtn_event():
            password = generate_password()
            genOutput.config(text=password)
            pyperclip.copy(password)
            genBtn.config(text="Пароль скопирован", command=NONE)
            
def click_svBtn_event():
    value = newPassw.get()
    if len(value) < 12:
        alertMess1.config(text = 'Минимальная длинна пароля - 12 символов')

    else:

        alertMess1.config(text = '')       
        new_passw_win.destroy()
        create_note_win()  

def click_chngPasswBtn_event():
    note_win.destroy()
    create_chng_passw_win()
    
def click_verefBtn_event():
    password = verefPassw.get()
    hashed_input = hashlib.sha256(password.encode()).hexdigest() # Хеширование введенного пароля 
    if hashed_input == file_content:
        veref_win.destroy()
        create_note_win()

    
def click_bckToNtBtn_event():
    chng_passw_win.destroy()
    create_note_win()

def click_svChngBtn_event():
    new_password = chngPassw.get()
    confirm_password = confPassw.get()

    if new_password == confirm_password:
        hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
        with open(find_check_verification_path(), "w") as file:
            file.write(hashed_new_password)
        alertMess2.config(text="Пароль успешно изменен!")
    else:
        alertMess2.config(text="Пароли не совпадают. Попробуйте снова.")

# create_chng_passw_win()      
create_new_passw_win()
# create_veref_win()
# create_note_win()



# try:

with open(find_check_verification_path(), "r") as file: # Читаем содержимое файла
        file_content = file.read().strip()  # Удаляем пробельные символы с начала и конца строки
        hachPassword = bool(file_content)  # Флаг, указывающий на наличие пароля

# except FileNotFoundError: hachPassword = False  # Флаг, указывающий на отсутствие пароля
# except Exception as e:
#     print(f"Ошибка при чтении файла: {e}")
#     hachPassword = False

# if hachPassword:
#     create_veref_win()
#     password =  
#     hashed_input = hashlib.sha256(password.encode()).hexdigest() # Хеширование введенного пароля 
#     if hashed_input == file_content: # Сравнение хешей
#         print("Доступ разрешен!")


#         filename = find_check_data_path()  # Имя файла, который нужно зашифровать/расшифровать

#         # Процесс шифровки/дешифровки
#         while True:
#             with open("Safety-Island/begin/docs/state.txt", "r") as file:
#                 state = file.read().strip()

#             if state == "decrypted":
#                 choice = input("Расшифровать (Y)? ")
#                 if choice.lower() == 'y':
#                     decrypt_file(filename, password)
#                     print(f"Файл {filename} расшифрован.")
#                     fernet_decrypt_file(find_check_data_path(), generate_key_from_password(password))
#                     update_state("Safety-Island/begin/docs/state.txt", "encrypted")  # Обновляем состояние

#                     # Логика смены пароля
#                     new_password = input("Сменить пароль (Y)? ")
#                     if new_password.lower() == 'y':
#                         password = input("Введите новый пароль: ")
#                         with open(find_check_verification_path(), "w") as file:
#                                 file.write(hashlib.sha256(password.encode()).hexdigest())
#                         password = None  # Обнуляем переменную с паролем
#                         print("Пароль изменен.")
#                     else:
#                         print("Смена пароля отклонена")
#                         password = None  # Обнуляем переменную с паролем
                    
#                     choice2 = input("Шифровать (Y)? ")
#                     if choice2.lower() == 'y':
#                         fernet_encrypt_file('Safety-Island/begin/docs/data.txt', generate_key_from_password(password))
#                         encrypt_file(filename, password)
#                         print(f"Файл {filename} зашифрован.")
#                         password = None  # Обнуляем переменную с паролем
#                         update_state("Safety-Island/begin/docs/state.txt", "decrypted")  # Обновляем состояние
#                     break  # Выходим из цикла
#                 else:
#                     print("Некорректный выбор")


#             password = None # Обнуляем переменную с паролем
#             break
#     else:
#         print("В доступе отказано. Попробуйте ещё раз.")

#     password = None # Обнуляем переменную с паролем
    
# else: 
#     create_new_passw_win()
#     password = newPassw.get()
    
#     # Хеширование пароля
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()

#     # Запись хешированного пароля в файл
#     try:
#         with open(find_check_verification_path(), "w") as file:
#             file.write(hashed_password)

#         filename = find_check_data_path  # Имя файла, который нужно зашифровать/расшифровать

#         # Процесс шифровки/дешифровки
#         while True:
#             choice = input("Шифровать (Y)? ")
        
#             if choice.lower() == 'y':
#                 fernet_encrypt_file(find_check_data_path(), generate_key_from_password(password))
#                 encrypt_file(filename, password)
#                 print(f"Файл {filename} зашифрован.")
#                 password = None # Обнуляем переменную с паролем
#                 with open("Safety-Island/begin/docs/state.txt", "w") as file:
#                     file.write("decrypted")
#                 break
#             else: print("Некорректный выбор")

#     except Exception as e:
#         print(f"Ошибка при записи пароля в файл: {e}")

#     password = None # Обнуляем переменную с паролем