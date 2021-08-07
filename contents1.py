from constants import *
import contents2
import app


global button_list


def login_contents(frame):
    def frame_event(e):
        if e1.get() == '' or e1.get() == ' Account Number':
            e1.delete(0, END)
            e1.insert(0, ' Account Number')
            e1.config(fg=color_silver, insertbackground='white')
        if e2.get() == '' or e2.get() == ' Password':
            e2.delete(0, END)
            e2.insert(0, ' Password')
            e2.config(fg=color_silver, insertbackground='white')

    def event_in_1(e):
        if e1.get() == ' Account Number':
            e1.delete(0, END)
            e1.config(fg='black', insertbackground='black')

    def event_out_1(e):
        if e1.get() == '':
            e1.insert(0, ' Account Number')
            e1.config(fg=color_silver, insertbackground='white')

    def event_in_2(e):
        if e2.get() == ' Password':
            e2.delete(0, END)
            e2.config(fg='black', insertbackground='black')

    def event_out_2(e):
        if e2.get() == '':
            e2.insert(0, ' Password')
            e2.config(fg=color_silver)

    color_silver = 'silver'
    frame.bind("<Button-1>", frame_event)

    topbar_contents = {'About': app.about,
                       'Help': app.home}
    logo_img = logo(230, file='transparent2.png')
    logo_label = Label(frame, image=logo_img, bd=0, bg=color_bg)
    logo_label.place(x=w / 2 - 230 / 2, y=25)
    topbar(frame, topbar_contents)

    Y_REF = 250

    e1_frame = Frame(frame, bg='silver')
    e1_frame.place(x=w / 2 - 250 / 2 - 1, y=Y_REF - 1, width=252, height=27)
    e1 = Entry(frame, bd=0, insertbackground='white', font=("Lato", 10,))
    e1.place(x=w / 2 - 250 / 2, y=Y_REF, width=250, height=25)
    e1.bind('<FocusIn>', event_in_1)
    e1.bind('<FocusOut>', event_out_1)
    e1.bind("<Button-1>", event_in_1)
    e1.insert(0, ' Account Number')
    e1.config(fg=color_silver)

    e2_frame = Frame(frame, bg='silver')
    e2_frame.place(x=w / 2 - 250 / 2 - 1, y=Y_REF + 40 - 1, width=252, height=27)
    e2 = Entry(frame, bd=0, insertbackground='white', font=("Lato", 10,))
    e2.place(x=w / 2 - 250 / 2, y=Y_REF + 40, width=250, height=25)
    e2.bind('<FocusIn>', event_in_2)
    e2.bind('<FocusOut>', event_out_2)
    e2.bind("<Button-1>", event_in_2)
    e2.insert(0, ' Password')
    e2.config(fg=color_silver)

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
                               activebackground=color_bg, fg='#3A89ED',command=app.Interface.newaccount_window)
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
        ' Profile': app.profile,
        ' Check Balance': app.check_balance,
        ' View Transactions': app.view_transactions,
        ' Online Transfer': app.online_transfer,
        ' Deposit': app.deposit,
        ' Withdraw': app.withdraw,
        ' Investments': app.investments,
        ' Personal Loans': app.personal_loans
    }
    button_list = sidebar(frame1, sidebar_contents)

    Label(frame, text='Welcome', font=("Lato", 10,), bg=color_bg, anchor='w').place(x=90, y=50, width=100, height=20)
    Label(frame, text=name.title(), font=("Lato", 12, 'italic'), bg=color_bg, anchor='w', fg='purple').place(x=90, y=75,
                                                                                                             width=150,
                                                                                                             height=20)


