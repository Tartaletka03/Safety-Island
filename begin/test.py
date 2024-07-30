from tkinter import *
from tkinter import ttk        

authorization = Tk()
authorization.title('SafeNote')
authorization.geometry('300x250+400+400')
authorization.resizable(False, False)

Label(text='Введите пароль:').pack(pady=20)
passw = ttk.Entry(width=35)
passw.pack(pady=10)
alertMess = Label(text='')
alertMess.pack()
Label().pack()
svBtn = ttk.Button(text='Войти')
svBtn.pack()

authorization.mainloop()