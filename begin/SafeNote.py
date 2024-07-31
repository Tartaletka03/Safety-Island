from script import *
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import pyperclip

def create_new_passw_win():
    global new_passw_win, passw, alertMess
    new_passw_win = Tk()
    new_passw_win.title('SafeNote')
    new_passw_win.geometry('300x250+400+400')
    new_passw_win.resizable(False, False)

    Label(text='Придумайте пароль:').pack(pady=20)
    passw = ttk.Entry(width=35)
    passw.pack(pady=10)
    alertMess = Label(text='')
    alertMess.pack()
    Label().pack()
    svBtn = ttk.Button(text='Сохранить', command=click_save_event)
    svBtn.pack(pady=30)

    new_passw_win.mainloop()

def click_save_event():
    value = passw.get()
    if len(value) < 12:
        alertMess.config(text = 'Минимальная длинна пароля - 12 символов')

    else:
        def click_gen_event():
            password = generate_password()
            genOutput.config(text=password)
            pyperclip.copy(password)
            genBTN.config(text="Пароль скопирован", command=NONE)
        
        def click_chng_event():
            note_win.destroy()
            create_new_passw_win()
            
        new_passw_win.destroy()  

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
        chngBTN = ttk.Button(text='Изменить пароль', command=click_chng_event)
        chngBTN.place(x=20, y=420)
        genBTN = ttk.Button(text='Сгенерировать пароль', width=21, command=click_gen_event)
        genBTN.place(x=140, y=420)

        note_win.mainloop()

create_new_passw_win()