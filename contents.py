import operations
from Application import *

global button_list


def login_contents(frame):
    def frame_event(e):
        if login_accountnumber_entry.get() == '' or login_accountnumber_entry.get() == ' Account Number':
            login_accountnumber_entry.delete(0, END)
            login_accountnumber_entry.insert(0, ' Account Number')
            login_accountnumber_entry.config(fg=color_silver, insertbackground='white')
        if login_password_entry.get() == '' or login_password_entry.get() == ' Password':
            login_password_entry.delete(0, END)
            login_password_entry.insert(0, ' Password')
            login_password_entry.config(fg=color_silver, insertbackground='white')

    def event_in_1(e):
        if login_accountnumber_entry.get() == ' Account Number':
            login_accountnumber_entry.delete(0, END)
            login_accountnumber_entry.config(fg='black', insertbackground='black')

    def event_out_1(e):
        if login_accountnumber_entry.get() == '':
            login_accountnumber_entry.insert(0, ' Account Number')
            login_accountnumber_entry.config(fg=color_silver, insertbackground='white')

    def event_in_2(e):
        if login_password_entry.get() == ' Password':
            login_password_entry.delete(0, END)
            login_password_entry.config(fg='black', insertbackground='black')

    def event_out_2(e):
        if login_password_entry.get() == '':
            login_password_entry.insert(0, ' Password')
            login_password_entry.config(fg=color_silver)

    color_silver = 'silver'
    frame.bind("<Button-1>", frame_event)

    topbar_contents = {'About': App.about,
                       'Help': App.home}
    global logo_img1, logo_label1
    logo_img1 = logo(230, file='transparent2.png')
    logo_label1 = Label(frame, image=logo_img1, bd=0, bg=color_bg)
    logo_label1.place(x=w / 2 - 230 / 2, y=25)
    topbar(frame, topbar_contents)

    Y_REF = 250

    e1_frame = Frame(frame, bg='silver')
    e1_frame.place(x=w / 2 - 250 / 2 - 1, y=Y_REF - 1, width=252, height=27)

    login_accountnumber_entry = Entry(frame, bd=0, insertbackground='white', font=("Lato", 10,))
    login_accountnumber_entry.place(x=w / 2 - 250 / 2, y=Y_REF, width=250, height=25)
    login_accountnumber_entry.bind('<FocusIn>', event_in_1)
    login_accountnumber_entry.bind('<FocusOut>', event_out_1)
    login_accountnumber_entry.bind("<Button-1>", event_in_1)
    login_accountnumber_entry.insert(0, ' Account Number')
    login_accountnumber_entry.config(fg=color_silver)

    e2_frame = Frame(frame, bg='silver')
    e2_frame.place(x=w / 2 - 250 / 2 - 1, y=Y_REF + 40 - 1, width=252, height=27)

    login_password_entry = Entry(frame, bd=0, insertbackground='white', font=("Lato", 10,))
    login_password_entry.place(x=w / 2 - 250 / 2, y=Y_REF + 40, width=250, height=25)
    login_password_entry.bind('<FocusIn>', event_in_2)
    login_password_entry.bind('<FocusOut>', event_out_2)
    login_password_entry.bind("<Button-1>", event_in_2)
    login_password_entry.insert(0, ' Password')
    login_password_entry.config(fg=color_silver)

    button_login = Button(frame, bd=0, text='Log in', bg='#175C4C', fg='white', activebackground='#1B6A58',
                          activeforeground='white', font=("Lato", 10, 'bold'))
    button_login.place(x=w / 2 - 250 / 2, y=Y_REF + 80 + 10, width=250, height=27)

    Label(frame, text='___________________\t\t___________________', fg=color_silver, bg=color_bg).place(
        x=w / 2 - 260 / 2,
        y=390, width=260,
        height=20)
    Label(frame, text='or', fg=color_silver, bg=color_bg, font=("Lato", 11,)).place(x=w / 2 - 20 / 2, y=393, width=20,
                                                                                    height=20)

    button_forget = Button(frame, text='Forgot your password?', font=("Lato", 10,), bd=0, bg=color_bg,
                           activebackground=color_bg, fg='#3A89ED')
    button_forget.place(width=250, height=25, x=w / 2 - 250 / 2, y=420)

    button_newaccount = Button(frame, text='Create a new account', font=("Lato", 10,), bd=0, bg=color_bg,
                               activebackground=color_bg, fg='#3A89ED', command=lambda: App.newaccount_window(frame))
    button_newaccount.place(width=250, height=25, x=w / 2 - 250 / 2, y=450)


def main_contents(frame, frame1, frame2, name):
    global button_list
    topbar_contents = {'About': '',
                       'Settings': '',
                       'Help': '',
                       'Logout': '',
                       }
    topbar(frame, topbar_contents)

    sidebar_contents = {
        ' Profile': App.profile,
        ' Check Balance': App.check_balance,
        ' View Transactions': App.view_transactions,
        ' Online Transfer': App.online_transfer,
        ' Deposit': App.deposit,
        ' Withdraw': App.withdraw,
        ' Investments': App.investments,
        ' Personal Loans': App.personal_loans
    }
    button_list = sidebar(frame1, sidebar_contents)

    Label(frame, text='Welcome', font=("Lato", 10,), bg=color_bg, anchor='w').place(x=90, y=50, width=100, height=20)
    Label(frame, text=name.title(), font=("Lato", 12, 'italic'), bg=color_bg, anchor='w', fg='purple').place(x=90, y=75,
                                                                                                             width=150,
                                                                                                             height=20)



