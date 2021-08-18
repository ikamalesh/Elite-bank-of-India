from tkinter import *

root = Tk()
frame=Frame(root,width=100,heigh=100,bd=11)
frame.pack()
label = Label(frame,text="Enter a digit that you guessed:").pack()
entry= Entry(frame,bd=4)
entry.pack()
entry.focus()
button1=Button(root,width=4,height=1,text='ok')
button1.pack()

root.mainloop()