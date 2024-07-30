from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def click_event1():
    value = passw.get()
    if len(value) < 12:
        
        alertMess.config(text = 'Минимальная длинна пароля - 12 символов')
    else:
        root.destroy()  

        new_win = Tk()
        new_win.title("SafeNote")
        new_win.geometry("300x420+400+400")
        new_win.resizable(True, False)
        new_win.minsize(300, 420)
        new_win.maxsize(500, 420)

        editor = ScrolledText()
        editor.pack()
        svBtn = ttk.Button(text='Сохранить')
        svBtn.pack(pady=3)

        new_win.mainloop()
        

root = Tk()
root.title('SafeNote')
root.geometry('300x250+400+400')
root.resizable(False, False)

Label(text='Придумайте пароль:').pack(pady=20)
passw = ttk.Entry(width=35)
passw.pack(pady=10)
alertMess = Label(text='')
alertMess.pack()
Label().pack()
svBtn = ttk.Button(text='Сохранить', command=click_event1)
svBtn.place(x=42, y=170)
genBTN = ttk.Button(text='Сгенерировать пароль')
genBTN.place(x=123, y=170)

root.mainloop()