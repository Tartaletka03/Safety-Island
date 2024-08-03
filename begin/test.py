import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext

def load_file():
    # Открываем диалог выбора файла
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"),
                                                      ("All files", "*.*")])
    # Если файл выбран, загружаем его содержимое
    if file_path:
        with open(file_path, 'r') as file:
            text_content = file.read()
            editor.delete("1.0", tk.END)  # Очищаем текущий текст в виджете
            editor.insert(tk.END, text_content)  # Вставляем новый текст

# Создаем основное окно
root = tk.Tk()
root.title("Текстовый редактор")

# Создаем виджет ScrolledText
editor = scrolledtext.ScrolledText(root, wrap=tk.WORD)
editor.pack(expand=True, fill='both')

# Создаем кнопку "Загрузить"
load_button = tk.Button(root, text="Загрузить файл", command=load_file)
load_button.pack()

# Запускаем основной цикл приложения
root.mainloop()