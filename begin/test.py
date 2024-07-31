from tkinter import *

window = Tk()
window.title("Калькулятор")
window.geometry("400x600")
window.resizable(False, False)
canvas = Canvas(window, width=400, height=400, bg='white')

font_settings = ("Times New Roman", 40, "")
virtualImg = PhotoImage()


resultLabel = Label(window, text="0", font=font_settings, image=virtualImg, width=380, height=75, compound=CENTER, bg="grey77", anchor='e')
resultLabel.place(x=10, y=10)
genOutput = Label(window, text='1111', width=380, height=75, compound=CENTER, justify=RIGHT)
genOutput.place(x=10, y=20)

mainloop()