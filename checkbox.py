from tkinter import *

window =Tk()
lbl = Label(window, text='Choose your favorite programming languages:')
frame = Frame (window)
python = Checkbutton(frame, text='Python')
javascript = Checkbutton(frame, text='javascript')
rust = Checkbutton(frame, text='rust')
typescript = Checkbutton(frame, text='typescript')


lbl.pack()
frame.pack()
python.pack()
javascript.pack()
rust.pack()
typescript.pack()


window.mainloop()

