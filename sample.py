from tkinter import *

from tkvideo import tkvideo

root = Tk()
my_label = Label(root, bg='white')
my_label.pack()
player = tkvideo("assets/sample4.2.gif", my_label, loop=1, size=(225, 225))
player.play()

root.mainloop()
