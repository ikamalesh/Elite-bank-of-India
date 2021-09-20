import operations
from Application import *

#global button_list


def login_contents(frame):
    color_silver = 'silver'

    topbar_contents = {'About': App.about,
                       'Help': App.home}

    topbar(frame, topbar_contents)

    global img1, imglabel1
    img1 = logo(width=400, height=200, file='wholecrop.png', resize=False)
    imglabel1 = Label(frame, image=img1, bd=0, bg=color_bg)
    #old imglabel1.place(x=w / 2 - 150, y=110)
    imglabel1.place(x=w / 2 - 250, y=50)

    Y_REF = 350

    l1 = Label(frame, text='Account number', font=("Lato", 10), bd=0, bg=color_bg, fg=color_silver, anchor='w')
    l1.place(x=w / 2 - 250 / 2, y=Y_REF - 25, width=250, height=25)

    e1_frame = Frame(frame, bg=color_silver)
    login_accountnumber_entry = Entry(frame, bd=0, font=("Lato", 10,))

    e1_frame.place(x=w / 2 - 250 / 2 - 1, y=Y_REF - 1, width=252, height=27)
    login_accountnumber_entry.place(x=w / 2 - 250 / 2, y=Y_REF, width=250, height=25)

    l2 = Label(frame, text='Password', font=("Lato", 10), bd=0, bg=color_bg, fg=color_silver, anchor='w')
    l2.place(x=w / 2 - 250 / 2, y=Y_REF + 60 - 25, width=250, height=25)

    e2_frame = Frame(frame, bg=color_silver)
    login_password_entry = Entry(frame, bd=0, font=("Lato", 10,))

    e2_frame.place(x=w / 2 - 250 / 2 - 1, y=Y_REF + 60 - 1, width=252, height=27)
    login_password_entry.place(x=w / 2 - 250 / 2, y=Y_REF + 60, width=250, height=25)

    def login_click():
        accno = login_accountnumber_entry.get().upper()
        password = login_password_entry.get()
        operations.signin(frame, accno, password)

    button_login = Button(frame, bd=0, text='Login', bg='#B3E982', fg='#283556', activebackground='#BCEC91',
                          activeforeground='#283556', font=("Lato", 10, 'bold'), cursor='hand2', command=login_click)
    button_login.place(x=w / 2 - 250 / 2, y=Y_REF + 80 + 30, width=250, height=27)

    Label(frame, text='___________________\t\t___________________', fg=color_silver, bg=color_bg).place(
        x=w / 2 - 260 / 2,
        y=Y_REF + 390 - 230, width=260,
        height=20)
    Label(frame, text='or', fg=color_silver, bg=color_bg, font=("Lato", 11,)).place(x=w / 2 - 20 / 2, y=Y_REF + 393 - 230, width=20,height=20)

    button_forget = Button(frame, text='Forgot your password?', font=("Lato", 10,), bd=0, bg=color_bg, activebackground=color_bg, fg='#3A89ED', cursor='hand2')
    button_forget.place(width=250, height=25, x=w / 2 - 250 / 2, y=Y_REF + 420 - 230)

    button_newaccount = Button(frame, text='Create a new account', font=("Lato", 10,), bd=0, bg=color_bg, activebackground=color_bg, fg='#3A89ED', command=lambda: App.newaccount_window(frame),cursor='hand2')
    button_newaccount.place(width=250, height=25, x=w / 2 - 250 / 2, y=Y_REF + 450 - 230)


def main_contents(frame, framel, accno):
    global button_list
    topbar_contents = {'About': '',
                       'Settings': '',
                       'Help': '',
                       'Logout': '',
                       }
    topbar(frame, topbar_contents)

    sidebar_contents = {
        ' Profile': lambda: App.profile(frame,data=operations.profile_datagenerator(accno)),
        ' Check Balance': lambda: App.check_balance(frame,0),
        ' View Transactions': App.view_transactions,
        ' Online Transfer': App.online_transfer,
        ' Deposit': App.deposit,
        ' Withdraw': App.withdraw,
        ' Investments': App.investments,
        ' Personal Loans': App.personal_loans
    }
    button_list = sidebar(framel, sidebar_contents)
    App.profile(frame,data=operations.profile_datagenerator(accno))

    global img3, imglabel3
    img3 = logo(width=70, height=70, file='logo.png', resize=True)
    imglabel3 = Label(frame, image=img3, bd=0, bg=color_bg)
    imglabel3.place(x=10, y=40)

    Label(frame, text='Welcome', font=("Lato", 10,), bg=color_bg, anchor='w').place(x=90, y=50, width=100, height=20)
    Label(frame, text=operations.profile_datagenerator(accno)['firstname'].title(), font=("Lato", 12, 'italic'), bg=color_bg, anchor='w', fg='purple').place(x=90, y=75, width=140,  height=20)


