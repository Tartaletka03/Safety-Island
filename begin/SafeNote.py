from script import *
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import pyperclip



def create_new_passw_win():
    global new_passw_win, newPassw, newAlertMess, confNewPassw
    new_passw_win = Tk()
    new_passw_win.title('SafeNote')
    new_passw_win.geometry('300x250+400+400')
    new_passw_win.resizable(False, False)

    Label(text='Придумайте пароль:').pack(pady=10)
    newPassw = ttk.Entry(width=35)
    newPassw.pack()
    Label(text='Введите пароль ещё раз:').pack(pady=10)
    confNewPassw = ttk.Entry(width=35)
    confNewPassw.pack()
    newAlertMess = Label(text='')
    newAlertMess.pack(pady=10)
    svBtn = ttk.Button(text='Сохранить', command=click_svBtn_event)
    svBtn.pack(pady=25)

    new_passw_win.mainloop()

def create_veref_win():
    global veref_win, verefPassw, verefAlertMess
    veref_win = Tk()
    veref_win.title('SafeNote')
    veref_win.geometry('300x250+400+400')
    veref_win.resizable(False, False)

    Label(text='Введите пароль:').pack(pady=20)
    verefPassw = ttk.Entry(width=35)
    verefPassw.pack(pady=10)
    verefAlertMess = Label(text='')
    verefAlertMess.pack()
    Label().pack()
    verefBtn = ttk.Button(text='Войти', command=click_verefBtn_event)
    verefBtn.pack(pady=30)

    veref_win.mainloop()

def create_note_win():
    dec(value)
    load_data()
    global note_win, genOutput, editor, genBtn, isNote
    isNote = True
    note_win = Tk()
    note_win.title("SafeNote")
    note_win.geometry("300x450+400+400")
    note_win.resizable(False, False)
    note_win.protocol("WM_DELETE_WINDOW", exit_event)

    editor = ScrolledText()
    editor.pack()
    svTxtBtn = ttk.Button(text='Сохранить', command=click_svTxtBtn_event)
    svTxtBtn.place(x=20, y=392)
    genOutput = Label(text='', anchor='e', width=23)
    genOutput.place(x=108, y=393)
    chngPasswBtn = ttk.Button(text='Изменить пароль', command=click_chngPasswBtn_event)
    chngPasswBtn.place(x=20, y=420)
    genBtn = ttk.Button(text='Сгенерировать пароль', width=21, command=click_genBtn_event)
    genBtn.place(x=140, y=420)

    note_win.mainloop()

def create_chng_passw_win():
    global chng_passw_win, confPassw, chngPassw, chngAlertMess, isNote
    isNote = False
    chng_passw_win = Tk()
    chng_passw_win.title('SafeNote')
    chng_passw_win.geometry('300x250+400+400')
    chng_passw_win.resizable(False, False)
    chng_passw_win.protocol("WM_DELETE_WINDOW", exit_event)

    Label(text='Введите новый пароль:').pack(pady=10)
    chngPassw = ttk.Entry(width=35)
    chngPassw.pack()
    Label(text='Введите новый пароль ещё раз:').pack(pady=10)
    confPassw = ttk.Entry(width=35)
    confPassw.pack()
    chngAlertMess = Label(text='')
    chngAlertMess.pack(pady=10)
    svChngBtn = ttk.Button(text='Сохранить', command=click_svChngBtn_event)
    svChngBtn.place(x=150, y=195)
    bckToNtBtn = ttk.Button(text='Вернуться', command=click_bckToNtBtn_event)
    bckToNtBtn.place(x=70, y=195)

    chng_passw_win.mainloop()

def load_data():
    with open(find_path('data.txt'), 'r') as file:
        text_content = file.read()
        editor.insert(tk.END, text_content)

def click_genBtn_event():
            password = generate_password()
            genOutput.config(text=password)
            pyperclip.copy(password)
            genBtn.config(text="Пароль скопирован", command=NONE)
            
def click_svBtn_event():
    global value
    if confNewPassw.get() == '':
        if len(newPassw.get()) < 12:
            newAlertMess.config(text='Минимальная длинна пароля - 12 символов')
        else:
            newAlertMess.config(text='Заполните все поля')
    elif newPassw.get() != confNewPassw.get():
        newAlertMess.config(text='Пароли не совпадают')
    elif len(newPassw.get()) < 12:
        newAlertMess.config(text='Минимальная длинна пароля - 12 символов')
    else:
        value = newPassw.get()
        get_password(value)
        newAlertMess.config(text = '')       
        new_passw_win.destroy()
        create_note_win()  

def click_chngPasswBtn_event():
    note_win.destroy()
    create_chng_passw_win()
    
def click_verefBtn_event():
   global value
   if get_password(verefPassw.get()):
        value = verefPassw.get()
        create_note_win()
   else:
        verefAlertMess.config(text='Неверный пароль')
    
def click_svTxtBtn_event():
    text_content = editor.get("1.0", tk.END)
    with open(find_path('data.txt'), 'w') as file:
        file.write(text_content)

def click_bckToNtBtn_event():
    chng_passw_win.destroy()
    create_note_win()

def click_svChngBtn_event():
    if confPassw.get() == '':
        if len(chngPassw.get()) < 12:
            chngAlertMess.config(text='Минимальная длинна пароля - 12 символов')
        else:
            chngAlertMess.config(text='Заполните все поля')
    elif chngPassw.get() != confPassw.get():
        chngAlertMess.config(text='Пароли не совпадают')
    elif len(chngPassw.get()) < 12:
        chngAlertMess.config(text='Минимальная длинна пароля - 12 символов')
    else: 
        change_password(value, chngPassw.get())
 
def exit_event():
    if isNote:
        click_svTxtBtn_event()
        enc(value)
        value = None
        note_win.destroy()
    else:
        enc(value) 
        value = None
        chng_passw_win.destroy()
        


if TFpassword():
    create_veref_win()     
else:
    create_new_passw_win()

# create_chng_passw_win()      
# create_note_win()
# create_new_passw_win()



