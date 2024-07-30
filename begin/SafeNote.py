from tkinter import *
from tkinter import ttk

def click_event():
    value = passw.get()
    if len(value) < 12:
        
        alertMess.config(text = 'Минимальная длинна пароля - 12 символов')
    else:
        root.destroy()  

        new_win = Tk()
        new_win.title("SafeNote")
        new_win.geometry("300x250+500+500")
        
        editor = Text()
        editor.pack(fill=BOTH, expand=1)
        
        new_win.mainloop()
        

root = Tk()
root.title('SafeNote')
root.geometry('300x250+500+500')
root.resizable(False, False)

Label(text='Придумайте пароль:').pack(pady=20)
passw = ttk.Entry(width=35)
passw.pack(pady=10)
alertMess = Label(text='')
alertMess.pack()
Label().pack()
svBtn = ttk.Button(text='Сохранить', command=click_event)
svBtn.place(x=42, y=170)
genBTN = ttk.Button(text='Сгенерировать пароль')
genBTN.place(x=123, y=170)

root.mainloop()