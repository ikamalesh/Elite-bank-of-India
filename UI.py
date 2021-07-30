from tkinter import *
from PIL import Image, ImageTk


class interface():
    def __init__(self, window):
        w, h = 1100, 700
        window.geometry(f'{w}x{h}')
        # window.resizable(0, 0)
        bg = '#5271FF'
        lgFrame = Frame(window, bg=bg)
        lgFrame.place(x=0, y=0, width=w, height=h)

        Label(lgFrame, text='Username/ Acc No.', bg=bg, anchor="w").place(width=280, height=25, x=w / 2 - 280/2 , y=275)
        usernameEntry = Entry(lgFrame)
        usernameEntry.place(width=280, height=25, x=w / 2 - 280 / 2, y=300)

        passwordEntry = Entry(lgFrame)
        passwordEntry.place(width=280, height=25, x=w / 2 - 280 / 2, y=350)

        signinButton = Button(lgFrame, text='Login', bg='white', fg='black', font='calibri 12 bold', bd=0)
        signinButton.place(width=280, height=30, x=w / 2 - 280 / 2, y=400)


if __name__ == '__main__':
    window = Tk()
    app = interface(window)
    window.mainloop()
