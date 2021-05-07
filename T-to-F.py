# Переводим температуру по цельсию в Фаренгейты на GUI tkinter
from tkinter import *


def convert():
    convert = (int(entry.get()) - 32)*(5/9)
    label2.config(text=convert)


def quit():
    exit()


root = Tk()
root.title('Cels to Fahrenheit')
frame = Frame(root)
frame.pack()
label1 = Label(frame, text='Temperature in Fahrenheit:')
label1.pack()
entry = Entry(frame)
entry.pack()
label2 = Label(frame)
label2.pack()
button1 = Button(frame, text='Convert', command=convert, bg='teal')
button1.pack()
button2 = Button(frame, text='Quit', command=quit, bg='red')
button2.pack()

root.mainloop()
