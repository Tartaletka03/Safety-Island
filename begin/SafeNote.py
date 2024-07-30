from tkinter import *
from tkinter import ttk

def click_event():
    value = passw.get()
    if len(value) < 12:
        
        alertMess.config(text = 'Минимальная длинна пароля - 12 символов')
    else:
        print('Ok!')
        

root = Tk()
root.title('SafeNote')
root.geometry('300x250+500+500')
root.resizable(True, True)
root.minsize(300, 250)
root.maxsize(500, 500)


Label(text='Придумайте пароль').pack(pady=20)
passw = ttk.Entry(width=35)
passw.pack(pady=10)
alertMess = Label(text='')
alertMess.pack()
Label().pack()
ttk.Button(text='Сохранить', command=click_event).pack(pady=30)


root.mainloop()