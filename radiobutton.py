from tkinter import *

window =Tk()
lbl = Label(window, text='Gender:')
var = StringVar()
male = Radiobutton(window, text='Male', variable=var, value='M')
female = Radiobutton(window, text='Female', variable=var, value='Fm')

# frame = Frame (window)
# python = Checkbutton(frame, text='Python')
# javascript = Checkbutton(frame, text='javascript')
# rust = Checkbutton(frame, text='rust')
# typescript = Checkbutton(frame, text='typescript')


lbl.pack()
male.pack()
female.pack()
# frame.pack()
# python.pack()
# javascript.pack()
# rust.pack()
# typescript.pack()


window.mainloop()

