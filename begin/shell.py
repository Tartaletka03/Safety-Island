from tkinter import messagebox
import tkinter as tk
from tkinter import *
from script import *
import os

def create_password():
    global password
    def check_password():
        global password
        password = password_entry.get()
        confirm_password = confirm_entry.get()
        if password == confirm_password and len(password) >= 12:
            hidden_password(password)  # Сохраняем пароль
            password_window.destroy()
            openF()
        else:
            messagebox.showerror("Ошибка", "Пароли не совпадают или слишком короткий!")

    password_window = Tk()
    password_window.title("Создание пароля")

    password_window.geometry("420x150")
    screen_width = password_window.winfo_screenwidth()
    screen_height = password_window.winfo_screenheight()

    # Рассчитываем координаты для центрирования
    x = int((screen_width - 420) / 2)
    y = int((screen_height - 150) / 2)

    # Устанавливаем позицию окна
    password_window.geometry(f"+{x}+{y}")


    password_label = Label(password_window, text="Введите пароль:")
    password_label.grid(row=0, column=0, padx=10, pady=10)
    global password_entry  # Объявляем password_entry как глобальную
    password_entry = Entry(password_window, show="*")
    password_entry.grid(row=0, column=1, padx=10, pady=10)

    global show_password_button
    show_password_button = Button(password_window, text="Показать пароль", command=lambda: toggle_password(password_entry))  # Передаем password_entry
    show_password_button.grid(row=0, column=2, padx=10, pady=10)

    confirm_label = Label(password_window, text="Подтвердите пароль:")
    confirm_label.grid(row=1, column=0, padx=10, pady=10)
    global confirm_entry  # Объявляем confirm_entry как глобальную
    confirm_entry = Entry(password_window, show="*")
    confirm_entry.grid(row=1, column=1, padx=10, pady=10)

    global show_confirm_button
    show_confirm_button = Button(password_window, text="Показать пароль", command=lambda: toggle_confirm_password(confirm_entry))  # Передаем confirm_entry
    show_confirm_button.grid(row=1, column=2, padx=10, pady=10)

    confirm_button = Button(password_window, text="Подтвердить", command=check_password)
    confirm_button.grid(row=2, column=1, pady=10)

def check_password():
    global password
    def confirm_password():
        global password
        password = password_entry.get()
        if hidden_password(password):
            dec(password)
            password_window.destroy()
            openF()
        else:
            messagebox.showerror("Ошибка", "Неверный пароль!")

    password_window = Tk()
    password_window.title("Ввод пароля")

    password_window.geometry("385x100")
    screen_width = password_window.winfo_screenwidth()
    screen_height = password_window.winfo_screenheight()

    # Рассчитываем координаты для центрирования
    x = int((screen_width - 385) / 2)
    y = int((screen_height - 100) / 2)

    # Устанавливаем позицию окна
    password_window.geometry(f"+{x}+{y}")


    password_label = Label(password_window, text="Введите пароль:")
    password_label.grid(row=0, column=0, padx=10, pady=10)
    global password_entry
    password_entry = Entry(password_window, show="*")
    password_entry.grid(row=0, column=1, padx=10, pady=10)

    global show_password_button
    show_password_button = Button(password_window, text="Показать пароль", command=lambda: toggle_password(password_entry))  # Передаем password_entry
    show_password_button.grid(row=0, column=2, padx=10, pady=10)

    confirm_button = Button(password_window, text="Подтвердить", command=confirm_password)
    confirm_button.grid(row=1, column=1, pady=10)

# Функции для переключения отображения пароля
def toggle_password(entry):  # Принимаем entry как аргумент
    global show_password_button
    if entry.cget("show") == "*":
        entry.config(show="")
        show_password_button.config(text="Скрыть пароль")
    else:
        entry.config(show="*")
        show_password_button.config(text="Показать пароль")

def toggle_confirm_password(entry):  # Принимаем entry как аргумент
    global show_confirm_button
    if entry.cget("show") == "*":
        entry.config(show="")
        show_confirm_button.config(text="Скрыть пароль")
    else:
        entry.config(show="*")
        show_confirm_button.config(text="Показать пароль")




def openF():
    global root, text_area, password
    def save_file():
        global text_area, password
        """Сохраняет текст из текстового редактора в файл data.txt."""
        text = text_area.get("1.0", tk.END)
        with open(find_path("data.txt"), "w", encoding="utf-8") as f:
            f.write(text)
        root.destroy()  # Закрыть окно после сохранения
        enc(password)
        password = None

    def change_password():
        global password
        """Открывает диалоговое окно для ввода старого и нового паролей."""
        def confirm_change():
            global password
            new_password = new_password_entry.get()
            confirm_new_password = confirm_new_password_entry.get()
            if new_password == confirm_new_password and len(new_password) >= 12:
                change_password_internal(new_password)  # Вызываем внутреннюю функцию
                password = new_password
                change_password_window.destroy()
            else:
                messagebox.showerror("Ошибка", "Пароли не совпадают или слишком короткий!")

        change_password_window = tk.Toplevel(root)
        change_password_window.title("Изменить пароль")

        change_password_window.geometry("420x150")
        screen_width = change_password_window.winfo_screenwidth()
        screen_height = change_password_window.winfo_screenheight()

        # Рассчитываем координаты для центрирования
        x = int((screen_width - 420) / 2)
        y = int((screen_height - 150) / 2)

        # Устанавливаем позицию окна
        change_password_window.geometry(f"+{x}+{y}")


        new_password_label = tk.Label(change_password_window, text="Новый пароль:")
        new_password_label.grid(row=0, column=0, padx=10, pady=10)
        global password_entry
        new_password_entry = tk.Entry(change_password_window, show="*")
        new_password_entry.grid(row=0, column=1, padx=10, pady=10)

        global show_password_button
        show_password_button = Button(change_password_window, text="Показать пароль", command=lambda: toggle_password(new_password_entry))  # Передаем password_entry
        show_password_button.grid(row=0, column=2, padx=10, pady=10)


        confirm_new_password_label = Label(change_password_window, text="Подтвердите пароль:")
        confirm_new_password_label.grid(row=1, column=0, padx=10, pady=10)
        global confirm_entry  # Объявляем confirm_entry как глобальную
        confirm_new_password_entry = Entry(change_password_window, show="*")
        confirm_new_password_entry.grid(row=1, column=1, padx=10, pady=10)

        global show_confirm_button
        show_confirm_button = Button(change_password_window, text="Показать пароль", command=lambda: toggle_confirm_password(confirm_new_password_entry))  # Передаем confirm_entry
        show_confirm_button.grid(row=1, column=2, padx=10, pady=10)



        confirm_button = tk.Button(change_password_window, text="Изменить", command=confirm_change)
        confirm_button.grid(row=2, column=1, pady=10)
   
    def change_password_internal(new_password):
        with open(find_path("check_vertification.txt"), "w") as file:
            file.write(hashlib.sha256(new_password.encode()).hexdigest())


    root = tk.Tk()
    root.title("Блокнот")

    # Задаем размер окна (например, 600x400)
    root.geometry("600x400")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Рассчитываем координаты для центрирования
    x = int((screen_width - 600) / 2)
    y = int((screen_height - 400) / 2)

    # Устанавливаем позицию окна
    root.geometry(f"+{x}+{y}")

    text_area = tk.Text(root)
    text_area.pack(expand=True, fill="both")

    with open(find_path("data.txt"), "r", encoding="utf-8") as f:
        text = f.read()
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, text)

    # Создание меню
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Сохранить", command=save_file)
    menubar.add_cascade(label="Файл", menu=filemenu)

    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Изменить пароль", command=change_password)
    menubar.add_cascade(label="Изменить", menu=editmenu)

    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Сгенерировать пароль", command=lambda: append_password(f"\n{generate_password()}"))
    editmenu.add_command(label="Вырезать", command=lambda: text_area.event_generate("<<Cut>>"))
    editmenu.add_command(label="Копировать", command=lambda: text_area.event_generate("<<Copy>>"))
    editmenu.add_command(label="Вставить", command=lambda: text_area.event_generate("<<Paste>>"))
    menubar.add_cascade(label="Правка", menu=editmenu)

    def append_password(password):
        text_area.insert(tk.END, password)


    root.config(menu=menubar)
    root.protocol("WM_DELETE_WINDOW", save_file)  # Сохранить при закрытии окна
    root.mainloop()


if TFpassword():
    check_password()
else:
    create_password()

mainloop() 