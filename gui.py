from tkinter import *
from PIL import ImageTk, Image
window = Tk()
name = Label(window, text='PythonX - Learn Python', bg='white', fg='Blue', font=('Serif',16))
img = Image.open('download.jpg')
logo = ImageTk.PhotoImage(img)
image = Label(window, image=logo)

button = Button(window, text='Lets Start')
username = Label(window, text='Username')
font = ('Serif', 12)
inputBox = Entry(window)



name.pack()
image.pack()
username.pack(side=LEFT)
inputBox.pack(side=RIGHT)
button.place(x=100, y=350)
window.mainloop()

window2 = Tk()
frame = Frame(window2)
lbl = Label(frame, text='inside the frame')
btn = Button(frame, text='insite the frame')
frame.pack()
lbl.pack(side=TOP)
btn.pack(side=BOTTOM)
window2.mainloop()


