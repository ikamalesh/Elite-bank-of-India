from constants import *
import contents2
from Application import *
import csv
import operations

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
    global logo_img
    logo_img = logo(230, file='transparent2.png')
    logo_label = Label(frame, image=logo_img, bd=0, bg=color_bg)
    logo_label.place(x=w / 2 - 230 / 2, y=25)
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


def newaccount_contents(frame):
    global logo_img

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

    def file():
        global filename
        filename = filedialog.askopenfile(initialdir="/", title='Select a file', filetypes=(('PDF files', '*.pdf'),))
        filename = filename.name

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
    subframe = Frame(frame, bg=color_bg, bd=1, relief=SOLID)
    subframe.place(x=30, y=(h + 30) / 2 - 500 / 2, width=440, height=500)

    logo_img = logo(200, file='transparent2.png')
    logo_label = Label(frame, image=logo_img, bd=0, bg=color_bg)
    logo_label.place(x=(w + 30 + 440) / 2 - 200 / 2, y=100)
    Label(frame, text="Let's make money\nsimple", font=("times", 20), bg=color_bg).place(x=(w + 30 + 440) / 2 - 250 / 2,
                                                                                         y=70 + 250,
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

    ######LABELS
    l_firstname = Label(subframe, text='First name', font=font, bg=color_bg, anchor='w', fg='grey')
    l_lastname = Label(subframe, text='Last name', font=font, bg=color_bg, anchor='w', fg='grey')
    l_dob = Label(subframe, text='DOB (DD/MM/YYYY)', font=font, bg=color_bg, anchor='w', fg='grey')
    l_acctype = Label(subframe, text='Account type', font=font, bg=color_bg, anchor='w', fg='grey', )
    l_mobile = Label(subframe, text='Mobile number', font=font, bg=color_bg, anchor='w', fg='grey')
    l_email = Label(subframe, text='Email', font=font, bg=color_bg, anchor='w', fg='grey')
    l_gender = Label(subframe, text='Gender', font=font, bg=color_bg, anchor='w', fg='grey')
    l_nationality = Label(subframe, text='Nationality', font=font, bg=color_bg, anchor='w', fg='grey')
    l_address = Label(subframe, text='Address', font=font, bg=color_bg, anchor='w', fg='grey')
    l_pincode = Label(subframe, text='Pincode', font=font, bg=color_bg, anchor='w', fg='grey')
    l_district = Label(subframe, text='District', font=font, bg=color_bg, anchor='w', fg='grey')
    l_state = Label(subframe, text='State', font=font, bg=color_bg, anchor='w', fg='grey')
    l_kyc = Label(subframe, text='KYC Document', font=font, bg=color_bg, anchor='w', fg='grey')
    l_refno = Label(subframe, text='Reference No.', font=font, bg=color_bg, anchor='w', fg='grey')

    ######LABELS PLACE
    l_firstname.place(x=X_REF, y=Y_REF, width=100, height=25)
    l_lastname.place(x=X_REF + 220, y=Y_REF, width=100, height=25)
    l_dob.place(x=X_REF, y=Y_REF + 60, width=150, height=25)
    l_acctype.place(x=X_REF + 220, y=Y_REF + 60, width=150, height=25)
    l_mobile.place(x=X_REF, y=Y_REF + 120, width=150, height=25)
    l_email.place(x=X_REF + 220, y=Y_REF + 120, width=100, height=25)
    l_gender.place(x=X_REF, y=Y_REF + 180, width=150, height=25)
    l_nationality.place(x=X_REF + 220, y=Y_REF + 180, width=100, height=25)
    l_address.place(x=X_REF, y=Y_REF + 240, width=100, height=25)
    l_pincode.place(x=X_REF, y=Y_REF + 300, width=100, height=25)
    l_district.place(x=X_REF + 110, y=Y_REF + 300, width=100, height=25)
    l_state.place(x=X_REF + 270, y=Y_REF + 300, width=100, height=25)
    l_kyc.place(x=X_REF, y=Y_REF + 360, width=100, height=25)
    l_refno.place(x=X_REF + 240, y=Y_REF + 360, width=180, height=25)

    ######ENTRIES
    firstname = Entry(subframe, bd=1, relief=SOLID, font=font)
    lastname = Entry(subframe, bd=1, relief=SOLID, font=font)
    dob = Entry(subframe, bd=1, relief=SOLID, font=font)
    acctype1 = Radiobutton(subframe, text='Savings', variable=accounttype, font=font, bg=color_bg, value='Savings',
                           activebackground=color_bg, anchor='w')
    acctype2 = Radiobutton(subframe, text='Current', variable=accounttype, font=font, bg=color_bg, value='Current',
                           activebackground=color_bg)
    mobile = Entry(subframe, bd=1, relief=SOLID, font=font)
    email = Entry(subframe, bd=1, relief=SOLID, font=font)
    gender1 = Radiobutton(subframe, text='Male', variable=gender, font=font, bg=color_bg, value='Male',
                          activebackground=color_bg, anchor='w')
    gender2 = Radiobutton(subframe, text='Female', variable=gender, font=font, bg=color_bg, value='Female',
                          activebackground=color_bg)
    nation = Combobox(subframe, width=27, textvariable=nationality, state="readonly", font=font)
    nation['values'] = (' India', ' Sri Lanka', ' Bangladesh')
    nation["background"] = '#ff0000'
    address = Entry(subframe, bd=1, relief=SOLID, font=font)
    pincode = Entry(subframe, bd=1, relief=SOLID, font=font)
    pincode.bind("<FocusOut>", pincode_event)
    district = Entry(subframe, bd=1, relief=SOLID, font=font, state=DISABLED, disabledbackground="white",
                     disabledforeground="black")
    state = Entry(subframe, bd=1, relief=SOLID, font=font, state=DISABLED, disabledbackground="white",
                  disabledforeground="black")
    kyc_combo = Combobox(subframe, width=27, textvariable=kyc, state="readonly", font=font)
    kyc_combo['values'] = (' Aadhaar Card', ' Passport', ' Driving License')
    kyc_combo["background"] = '#ff0000'
    refno = Entry(subframe, bd=1, relief=SOLID, font=font, disabledbackground="white",
                  disabledforeground="black")

    ######ENTRIES PLACE
    firstname.place(x=X_REF, y=Y_REF + 25, width=200, height=25)
    lastname.place(x=X_REF + 220, y=Y_REF + 25, width=200, height=25)
    dob.place(x=X_REF, y=Y_REF + 60 + 25, width=200, height=25)
    acctype1.place(x=X_REF + 220, y=Y_REF + 60 + 25, width=100, height=25), acctype2.place(x=X_REF + 320,
                                                                                           y=Y_REF + 60 + 25, width=100,
                                                                                           height=25)
    mobile.place(x=X_REF, y=Y_REF + 120 + 25, width=200, height=25)
    email.place(x=X_REF + 220, y=Y_REF + 120 + 25, width=200, height=25)
    gender1.place(x=X_REF, y=Y_REF + 180 + 25, width=100, height=25), gender2.place(x=X_REF + 100, y=Y_REF + 180 + 25,
                                                                                    width=100, height=25)
    nation.place(x=X_REF + 220, y=Y_REF + 180 + 25, width=200, height=25)
    address.place(x=X_REF, y=Y_REF + 240 + 25, width=420, height=25)
    pincode.place(x=X_REF, y=Y_REF + 300 + 25, width=100, height=25)
    district.place(x=X_REF + 110, y=Y_REF + 300 + 25, width=150, height=25)
    state.place(x=X_REF + 270, y=Y_REF + 300 + 25, width=150, height=25)
    kyc_combo.place(x=X_REF, y=Y_REF + 360 + 25, width=150, height=25)
    refno.place(x=X_REF + 240, y=Y_REF + 360 + 25, width=180, height=25)

    upload = Button(subframe, text='Upload', bd=1, relief=SOLID, command=file)
    upload.place(x=X_REF + 160, y=Y_REF + 360 + 25, width=50, height=25)

    signup_button = Button(subframe, text='Sign up', bd=1, relief=SOLID, command=submit_button)
    signup_button.place(x=440 / 2 - 100 / 2, y=Y_REF + 420 + 25, width=100, height=25)
