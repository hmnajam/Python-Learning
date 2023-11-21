from tkinter import *

window = Tk()
window.geometry('600x270')
window.title('Employee Database')


empId = Label(window, text='Employee ID', font=('Serif', 12))
empId.place(x=20,y=30)
enterId = Entry(window)
enterId.place(x=170, y=30)



empName = Label(window, text='Employee Name', font=('Serif', 12))
empName.place(x=20,y=60)
enterName = Entry(window)
enterName.place(x=170, y=60)



empDept = Label(window, text='Employee Dept', font=('Serif', 12))
empDept.place(x=20,y=90)
enterDept = Entry(window)
enterDept.place(x=170, y=90)



window.mainloop()
