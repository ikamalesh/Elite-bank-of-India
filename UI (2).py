from ezgmail import *
from tkinter import *

from tkinter import ttk
from time import sleep
from PIL import Image, ImageTk
import ezsheets
from threading import *
from datetime import *
import itertools
# import beepy
from tkinter import messagebox


class interface():
    def __init__(self, window):
        window.geometry('900x600')
        window.resizable(0, 0)

        # Default layout
        bgimg = ImageTk.PhotoImage(Image.open('blue1.jpg'))
        Label(window, image=bgimg).place(x=0,y=0)


        global topframe, lframe, rframe, txtbox, msg, sendbutton, logoutbutton, image4, usernamelabel, logoutbutton, secondaryaddbutton, searchentry
        global variable1, bg, afterclickbutton_title, dead
        window.title('JusChat')
        bg = '#2178BF'
        topframe = Frame(window, width=900, height=55, bg=bg).place(x=0, y=0)  # 2196F3
        lframe = Frame(window, width=250, height=600 - 55, bg=bg).place(x=0, y=55)  # 7E93C8
        rframe = Frame(window, width=900 - 250, height=600 - 55, bg='white', relief=GROOVE, bd=3).place(x=250, y=55)
        Label(window, text='_' * 69, fg=bg, font='calibri 12 bold', bg='white').place(x=260, y=520)
        txtbox = Text(window, width=62, height=20, bd=0, bg='white', fg='black', font='calibri 13', relief=GROOVE)
        msg = Entry(window, width=47, bg='white', font='caliri 13', bd=0, )
        sendbutton = Button(window, text='SEND', width=7, font='calibri 12 bold', fg=bg, bg='white',
                            activebackground='white', bd=0,)
        image4 = ImageTk.PhotoImage(Image.open('user.png'))
        imglabel = Label(window, image=image4, bg=bg)

        txtbox.place(x=263, y=65), msg.place(x=263, y=555), sendbutton.place(x=810, y=555 - 5), imglabel.place(x=10,
                                                                                                               y=8)
        txtbox.config(state=DISABLED)
        msg.config(state=DISABLED)
        sendbutton.config(state=DISABLED)
        # Varying layout

        logoutbutton = Button(window, text='Logout', font='arial 10', bg=bg, bd=0, fg='light blue', activebackground=bg)
        logoutbutton.place(x=70, y=33)

        usernamelabel = Label(window, text='', font='arial 12 bold', bg=bg, fg='#F7CF5F')
        usernamelabel.place(x=70, y=10)

        secondaryaddbutton = Button(window, text='🔍', bd=0, width=5, bg=bg, font='arial 14 ',
                                    activebackground=bg, )
        searchentry = Entry(window, width=25, font='calibri 12')
        secondaryaddbutton.place(x=842, y=7), searchentry.place(x=620, y=15)

        afterclickbutton_title = Label(window, text='', bg=bg, fg='white', font='cailbri 17')
        afterclickbutton_title.place(x=250, y=15)

        ######EXTRA
        interface.login_page()


    def login_page():
        global image1, loginpage_frame, logo, icon, image2, userinput, passwordinput, loginbutton, forgotpasswordbutton, newuserbutton
        window.title('Login')
        w,h = 900, 600
        loginpage_frame = Frame(window, width=w, height=h, bg='#2196F3')
        loginpage_frame.place(x=0, y=0)

        image1 = ImageTk.PhotoImage(Image.open('ghost.png'))
        image2 = ImageTk.PhotoImage(Image.open('logo.png'))

        icon = Label(loginpage_frame, image=image1, bg='#2196F3')
        icon.place(x= w/2-32, y=70)

        logo = Label(loginpage_frame, image=image2, bg='#2196F3')
        logo.place(x= 700, y=10)


        Label(loginpage_frame, text='Username', fg='white', bg='#2196F3', font='arial').place(x=900, y=175)
        Label(loginpage_frame, text='Password', fg='white', bg='#2196F3', font='arial').place(x=900, y=235)
        userinput = Entry(loginpage_frame, width=30, font='calibri 13')
        passwordinput = Entry(loginpage_frame, width=30, font='calibri 13', show='●')
        userinput.place(x=900, y=900), passwordinput.place(x=900, y=900 + 60)

        loginbutton = Button(loginpage_frame, text='Login', font='calibri 12 bold', bg='white', bd=0, width=15,
                             )
        loginbutton.place(x=900 + 80, y=900 + 120)

        Label(loginpage_frame, text='_' * 45, bg='#2196F3', fg='white').place(x=900 + 40, y=900 + 190)

        forgotpasswordbutton = Button(loginpage_frame, text='Forgotten password?', bd=0, fg='darkblue', bg='#2196F3',
                                      activebackground='#2196F3', font='calibri',
                                      command=interface.forgottenpassword_page)
        forgotpasswordbutton.place(x=900 + 70, y=900 + 170)

        newuserbutton = Button(loginpage_frame, text='Create New Account', bg='light green', fg='black',
                               font='calibri 12', width=18, activebackground='#90DA90', bd=0,
                               command=interface.createnewaccount)
        newuserbutton.place(x=900 + 75, y=900 + 220)

    def forgottenpassword_page():
        global fp_frame, email_entry, cancelbutton, sendbutton
        fp_frame = Frame(loginpage_frame, width=900, height=600, bg='#2196F3')
        fp_frame.place(x=0, y=0)

        Frame(fp_frame, width=460, height=250, bg='white').place(x=225, y=160)

        Label(fp_frame, text='Find Your Account', font='calibri 16 bold', bg='white').place(x=235, y=170)
        Label(fp_frame, text='Please enter your email address to search for your account.',
              font='calibri 12', bg='white').place(x=235, y=240)

        email_entry = Entry(fp_frame, width=39, bd=1, font='calibri 15', relief=SOLID)
        email_entry.place(x=235, y=290)

        cancelbutton = Button(fp_frame, text='Cancel', font='calibri 12', bg='#E4E6EB', bd=1, width=8,
                              command=fp_frame.destroy)
        cancelbutton.place(x=590, y=360)

        sendbutton = Button(fp_frame, text='Send', font='calibri 12', bg='#2196F3', bd=1, width=8,
                            activebackground='#2188F3')
        sendbutton.place(x=500, y=360)

    def createnewaccount():
        global newpassentry, b, text, image3, newacc_frame, emailentry, usernameentry, signupbutton, friendslabel, image4, welcomelabel

        newacc_frame = Frame(loginpage_frame, bg='white', width=900, height=600)
        newacc_frame.place(x=0, y=0)

        Label(newacc_frame, text='Create a new account', font='calibri 22 bold', bg='white').place(x=20, y=30)
        Label(newacc_frame, text="It's quick and easy.", fg='grey40', bg='white', font='calibri 15').place(x=21, y=70)

        Label(newacc_frame, text='Email Address', font='calibri 11', bg='white', fg='grey40').place(x=19, y=125)
        emailentry = Entry(newacc_frame, width=30, font='calibri 13', relief=SOLID, bd=1)
        emailentry.place(x=20, y=150)

        Label(newacc_frame, text='New Username', font='calibri 11', bg='white', fg='grey40').place(x=19, y=195)
        usernameentry = Entry(newacc_frame, width=30, font='calibri 13', relief=SOLID, bd=1)
        usernameentry.place(x=20, y=220)

        Label(newacc_frame, text='New Password', font='calibri 11', bg='white', fg='grey40').place(x=19, y=265)
        newpassentry = Entry(newacc_frame, width=30, font='calibri 13', relief=SOLID, bd=1, show='●')
        newpassentry.place(x=20, y=290)

        Label(newacc_frame,
              text=f'By clicking Sign Up, you agree to our Terms, Data Policy and     \nCookie Policy. '
                   f'You may receive Email notifications from us'
                   f'       \nand can opt out at any time.\t\t\t\t'
              , font='calibri 8', bg='white', anchor="sw").place(x=20, y=350)

        cancelbutton = Button(newacc_frame, text='Back to Sign In ?', bg='white', fg='blue', font='calibri 10', bd=0,
                              activebackground='white', command=newacc_frame.destroy)
        cancelbutton.place(x=20, y=320)

        signupbutton = Button(newacc_frame, text='Sign Up', font='calibri 12', bg='#5E934A', bd=1, width=15,
                              activebackground='#5E8B4A', command=actions.adduserphase1)
        signupbutton.place(x=20, y=430)

        image3 = ImageTk.PhotoImage(Image.open('friends.jpg'))
        friendslabel = Label(newacc_frame, image=image3, bd=0)
        friendslabel.place(x=380, y=100)

        image4 = ImageTk.PhotoImage(Image.open('welcome.jpg'))
        welcomelabel = Label(newacc_frame, image=image4, bd=0)


if __name__ == '__main__':
    window = Tk()
    app = interface(window)
    window.mainloop()

