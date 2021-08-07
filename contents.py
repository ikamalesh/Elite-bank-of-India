from constants import *
import contents2
from Application import *
import csv
import operations

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

    topbar_contents = {'About': App.about,
                       'Help': App.home}
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


def newaccount_contents(frame):
    subframe = Frame(frame, bg=color_bg, bd=1, relief=SOLID)
    subframe.place(x=30, y=(h + 30) / 2 - 500 / 2, width=440, height=500)

    logo_img = logo(200, file='transparent2.png')
    logo_label = Label(frame, image=logo_img, bd=0, bg=color_bg)
    logo_label.place(x=(w + 30 + 440) / 2 - 200 / 2, y=100)

    Label(frame, text="Let's make money\nsimple", font=("times", 20),bg=color_bg).place(x=(w + 30 + 440) / 2 - 250 / 2, y=70 + 250,
                                                                           width=250)

    topbar_contents = {'< Back': frame.destroy, }

    topbar(frame, topbar_contents)

    X_REF = 10
    Y_REF = 10
    font = ("Lato", 10)

    accounttype = StringVar(value='Savings')
    gender = StringVar(value=1)
    nationality = StringVar()
    kyc = StringVar()

    def place():
        print(accounttype.get())

    def checkgender():
        print(gender.get())

    ######
    Label(subframe, text='First name', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF, y=Y_REF, width=100,
                                                                                            height=25)
    firstname = Entry(subframe, bd=1, relief=SOLID, font=font)
    firstname.place(x=X_REF, y=Y_REF + 25, width=200, height=25)

    ######
    Label(subframe, text='Last name', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF + 220, y=Y_REF,
                                                                                           width=100, height=25)
    lastname = Entry(subframe, bd=1, relief=SOLID, font=font)
    lastname.place(x=X_REF + 220, y=Y_REF + 25, width=200, height=25)

    ######
    Label(subframe, text='DOB (DD/MM/YYYY)', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF, y=Y_REF + 60,
                                                                                                  width=150, height=25)
    dob = Entry(subframe, bd=1, relief=SOLID, font=font)
    dob.place(x=X_REF, y=Y_REF + 60 + 25, width=200, height=25)

    ######
    Label(subframe, text='Account type', font=font, bg=color_bg, anchor='w', fg='grey', ).place(x=X_REF + 220,
                                                                                                y=Y_REF + 60, width=150,
                                                                                                height=25)
    Radiobutton(subframe, text='Savings', variable=accounttype, font=font, bg=color_bg, value='Savings', command=place,
                activebackground=color_bg, anchor='w').place(x=X_REF + 220, y=Y_REF + 60 + 25, width=100, height=25)
    Radiobutton(subframe, text='Current', variable=accounttype, font=font, bg=color_bg, value='Current', command=place,
                activebackground=color_bg).place(x=X_REF + 320, y=Y_REF + 60 + 25, width=100, height=25)

    ######
    Label(subframe, text='Mobile number', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF, y=Y_REF + 120,
                                                                                               width=150, height=25)
    mobile = Entry(subframe, bd=1, relief=SOLID, font=font)
    mobile.place(x=X_REF, y=Y_REF + 120 + 25, width=200, height=25)

    ######
    Label(subframe, text='Email', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF + 220, y=Y_REF + 120,
                                                                                       width=100, height=25)
    email = Entry(subframe, bd=1, relief=SOLID, font=font)
    email.place(x=X_REF + 220, y=Y_REF + 120 + 25, width=200, height=25)

    ######
    Label(subframe, text='Gender', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF, y=Y_REF + 180,
                                                                                        width=150, height=25)
    male = Radiobutton(subframe, text='Male', variable=gender, font=font, bg=color_bg, value='Male',
                       activebackground=color_bg, anchor='w', command=checkgender)
    male.place(x=X_REF, y=Y_REF + 180 + 25, width=100, height=25)
    female = Radiobutton(subframe, text='Female', variable=gender, font=font, bg=color_bg, value='Female',
                         activebackground=color_bg, command=checkgender)
    female.place(x=X_REF + 100, y=Y_REF + 180 + 25, width=100, height=25)

    #####
    Label(subframe, text='Nationality', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF + 220,
                                                                                             y=Y_REF + 180,
                                                                                             width=100, height=25)
    nation = Combobox(subframe, width=27, textvariable=nationality, state="readonly", font=font)
    nation['values'] = (' India', ' Sri Lanka', ' Bangladesh')
    nation["background"] = '#ff0000'
    nation.place(x=X_REF + 220, y=Y_REF + 180 + 25, width=200, height=25)

    #####
    Label(subframe, text='Address', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF, y=Y_REF + 240,
                                                                                         width=100,
                                                                                         height=25)
    address = Entry(subframe, bd=1, relief=SOLID, font=font)
    address.place(x=X_REF, y=Y_REF + 240 + 25, width=420, height=25)

    #####
    def pincode_event(e):
        pin = pincode.get()
        csv_file = csv.reader(open('india.csv', "r"), delimiter=",")
        for row in csv_file:
            if pin == row[0]:
                district.config(state=NORMAL)
                state.config(state=NORMAL)
                district.delete(0, END)
                state.delete(0, END)
                district.insert(0, row[1].title())
                state.insert(0, row[2].title())
                district.config(state=DISABLED)
                state.config(state=DISABLED)

    Label(subframe, text='Pincode', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF, y=Y_REF + 300,
                                                                                         width=100,
                                                                                         height=25)
    pincode = Entry(subframe, bd=1, relief=SOLID, font=font)
    pincode.place(x=X_REF, y=Y_REF + 300 + 25, width=100, height=25)
    pincode.bind("<FocusOut>", pincode_event)
    #####
    Label(subframe, text='District', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF + 110, y=Y_REF + 300,
                                                                                          width=100,
                                                                                          height=25)
    district = Entry(subframe, bd=1, relief=SOLID, font=font, state=DISABLED, disabledbackground="white",
                     disabledforeground="black")
    district.place(x=X_REF + 110, y=Y_REF + 300 + 25, width=150, height=25)

    #####
    Label(subframe, text='State', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF + 270, y=Y_REF + 300,
                                                                                       width=100, height=25)
    state = Entry(subframe, bd=1, relief=SOLID, font=font, state=DISABLED, disabledbackground="white",
                  disabledforeground="black")
    state.place(x=X_REF + 270, y=Y_REF + 300 + 25, width=150, height=25)

    #####
    Label(subframe, text='KYC Document', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF, y=Y_REF + 360,
                                                                                              width=100,
                                                                                              height=25)
    kyc_combo = Combobox(subframe, width=27, textvariable=kyc, state="readonly", font=font)
    kyc_combo['values'] = (' Aadhaar Card', ' Passport', ' Driving License')
    kyc_combo["background"] = '#ff0000'
    kyc_combo.place(x=X_REF, y=Y_REF + 360 + 25, width=150, height=25)

    def file():
        global filename
        filename = filedialog.askopenfile(initialdir="/", title='Select a file', filetypes=(('PDF files', '*.pdf'),))
        print(filename.name)

    upload = Button(subframe, text='Upload', bd=1, relief=SOLID, command=file)
    upload.place(x=X_REF + 160, y=Y_REF + 360 + 25, width=50, height=25)

    #####
    Label(subframe, text='Reference No.', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF + 240,
                                                                                               y=Y_REF + 360,
                                                                                               width=180, height=25)
    refno = Entry(subframe, bd=1, relief=SOLID, font=font, disabledbackground="white",
                  disabledforeground="black")
    refno.place(x=X_REF + 240, y=Y_REF + 360 + 25, width=180, height=25)

    def submit_button():
        operations.signup(
            firstname.get(),
            lastname.get(),
            dob.get(),
            gender.get(),
            address.get(),
            district.get(),
            state.get(),
            pincode.get(),
            nationality.get(),
            mobile.get(),
            email.get(),
            kyc.get(),
            refno.get(),
            filename,
            accounttype.get(),
        )

    submit = Button(subframe, text='Sign up', bd=1, relief=SOLID, command=submit_button)
    submit.place(x=440 / 2 - 100 / 2, y=Y_REF + 420 + 25, width=100, height=25)
