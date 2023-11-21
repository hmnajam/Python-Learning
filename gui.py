from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


def gui():
    window = Tk()
    name = Label(window, text='PythonX - Learn Python', bg='white', fg='Blue', font=('Serif',16))
    img = Image.open('download.jpg')
    logo = ImageTk.PhotoImage(img)
    image = Label(window, image=logo)

    frame = Frame(window)
    username = Label(frame, text='Username')
    font = ('Serif', 12)
    inputBox = Entry(frame)
    button = Button(window, text='Lets Start', command=showMessage)
    name.pack()
    image.pack()
    frame.pack()
    username.pack(side=LEFT)
    inputBox.pack(side=RIGHT)
    button.pack(side=BOTTOM)
    window.mainloop()

def showMessage():
    messagebox.showinfo('PythonX - Learn Python', 'Welcome')

if __name__=='__main__':
    gui()








# window2 = Tk()
# frame = Frame(window2)
# lbl = Label(frame, text='inside the frame')
# btn = Button(frame, text='insite the frame')
# frame.pack()
# lbl.pack(side=TOP)
# btn.pack(side=BOTTOM)
# window2.mainloop()


