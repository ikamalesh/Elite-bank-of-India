import operations
from Application import *

global button_list


def login_contents(frame):
    color_silver = 'silver'

    topbar_contents = {'About': App.about,
                       'Help': App.home}

    topbar(frame, topbar_contents)

    Y_REF = 300

    e1_frame = Frame(frame, bg='silver')
    login_accountnumber_entry = Entry(frame, bd=0, font=("Lato", 10,))

    e1_frame.place(x=w / 2 - 250 / 2 - 1, y=Y_REF - 1, width=252, height=27)
    login_accountnumber_entry.place(x=w / 2 - 250 / 2, y=Y_REF, width=250, height=25)

    e2_frame = Frame(frame, bg='silver')
    login_password_entry = Entry(frame, bd=0, font=("Lato", 10,))

    e2_frame.place(x=w / 2 - 250 / 2 - 1, y=Y_REF + 40 - 1, width=252, height=27)
    login_password_entry.place(x=w / 2 - 250 / 2, y=Y_REF + 40, width=250, height=25)

    button_login = Button(frame, bd=0, text='Log in', bg='#175C4C', fg='white', activebackground='#1B6A58',
                          activeforeground='white', font=("Lato", 10, 'bold'),cursor='hand2')
    button_login.place(x=w / 2 - 250 / 2, y=Y_REF + 80 + 10, width=250, height=27)

    Label(frame, text='___________________\t\t___________________', fg=color_silver, bg=color_bg).place(
        x=w / 2 - 260 / 2,
        y=Y_REF+390-250, width=260,
        height=20)
    Label(frame, text='or', fg=color_silver, bg=color_bg, font=("Lato", 11,)).place(x=w / 2 - 20 / 2, y=Y_REF+393-250, width=20,
                                                                                    height=20)

    button_forget = Button(frame, text='Forgot your password?', font=("Lato", 10,), bd=0, bg=color_bg,
                           activebackground=color_bg, fg='#3A89ED',cursor='hand2')
    button_forget.place(width=250, height=25, x=w / 2 - 250 / 2, y=Y_REF+420-250)

    button_newaccount = Button(frame, text='Create a new account', font=("Lato", 10,), bd=0, bg=color_bg,
                               activebackground=color_bg, fg='#3A89ED', command=lambda: App.newaccount_window(frame),cursor='hand2')
    button_newaccount.place(width=250, height=25, x=w / 2 - 250 / 2, y=Y_REF+450-250)


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



