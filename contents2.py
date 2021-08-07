from constants import *
import app
import csv


def newaccount_contents(frame):
    topbar_contents = {'< Back': frame.destroy, }

    topbar(frame, topbar_contents)

    X_REF = 230
    Y_REF = 50
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
    Label(frame, text='First name', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF, y=Y_REF, width=100,
                                                                                         height=25)
    firstname = Entry(frame, bd=1, relief=SOLID, font=font)
    firstname.place(x=X_REF, y=Y_REF + 25, width=200, height=25)

    ######
    Label(frame, text='Last name', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF + 220, y=Y_REF,
                                                                                        width=100, height=25)
    firstname = Entry(frame, bd=1, relief=SOLID, font=font)
    firstname.place(x=X_REF + 220, y=Y_REF + 25, width=200, height=25)

    ######
    Label(frame, text='DOB (DD/MM/YYYY)', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF, y=Y_REF + 60,
                                                                                               width=150, height=25)
    dob = Entry(frame, bd=1, relief=SOLID, font=font)
    dob.place(x=X_REF, y=Y_REF + 60 + 25, width=200, height=25)

    ######
    Label(frame, text='Account type', font=font, bg=color_bg, anchor='w', fg='grey', ).place(x=X_REF + 220,
                                                                                             y=Y_REF + 60, width=150,
                                                                                             height=25)
    Radiobutton(frame, text='Savings', variable=accounttype, font=font, bg=color_bg, value='Savings', command=place,
                activebackground=color_bg, anchor='w').place(x=X_REF + 220, y=Y_REF + 60 + 25, width=100, height=25)
    Radiobutton(frame, text='Current', variable=accounttype, font=font, bg=color_bg, value='Current', command=place,
                activebackground=color_bg).place(x=X_REF + 320, y=Y_REF + 60 + 25, width=100, height=25)

    ######
    Label(frame, text='Mobile number', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF, y=Y_REF + 120,
                                                                                            width=150, height=25)
    mobile = Entry(frame, bd=1, relief=SOLID, font=font)
    mobile.place(x=X_REF, y=Y_REF + 120 + 25, width=200, height=25)

    ######
    Label(frame, text='Email', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF + 220, y=Y_REF + 120,
                                                                                    width=100, height=25)
    email = Entry(frame, bd=1, relief=SOLID, font=font)
    email.place(x=X_REF + 220, y=Y_REF + 120 + 25, width=200, height=25)

    ######
    Label(frame, text='Gender', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF, y=Y_REF + 180,
                                                                                     width=150, height=25)
    male = Radiobutton(frame, text='Male', variable=gender, font=font, bg=color_bg, value='Male',
                       activebackground=color_bg, anchor='w', command=checkgender)
    male.place(x=X_REF, y=Y_REF + 180 + 25, width=100, height=25)
    female = Radiobutton(frame, text='Female', variable=gender, font=font, bg=color_bg, value='Female',
                         activebackground=color_bg, command=checkgender)
    female.place(x=X_REF + 100, y=Y_REF + 180 + 25, width=100, height=25)

    #####
    Label(frame, text='Nationality', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF + 220, y=Y_REF + 180,
                                                                                          width=100, height=25)
    nation = Combobox(frame, width=27, textvariable=nationality, state="readonly", font=font)
    nation['values'] = (' India', ' Sri Lanka', ' Bangladesh')
    nation["background"] = '#ff0000'
    nation.place(x=X_REF + 220, y=Y_REF + 180 + 25, width=200, height=25)

    #####
    Label(frame, text='Address', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF, y=Y_REF + 240, width=100,
                                                                                      height=25)
    address = Entry(frame, bd=1, relief=SOLID, font=font)
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

    Label(frame, text='Pincode', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF, y=Y_REF + 300, width=100,
                                                                                      height=25)
    pincode = Entry(frame, bd=1, relief=SOLID, font=font)
    pincode.place(x=X_REF, y=Y_REF + 300 + 25, width=100, height=25)
    pincode.bind("<FocusOut>", pincode_event)
    #####
    Label(frame, text='District', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF + 110, y=Y_REF + 300,
                                                                                       width=100,
                                                                                       height=25)
    district = Entry(frame, bd=1, relief=SOLID, font=font, state=DISABLED, disabledbackground="white",
                     disabledforeground="black")
    district.place(x=X_REF + 110, y=Y_REF + 300 + 25, width=150, height=25)

    #####
    Label(frame, text='State', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF + 270, y=Y_REF + 300,
                                                                                    width=100, height=25)
    state = Entry(frame, bd=1, relief=SOLID, font=font, state=DISABLED, disabledbackground="white",
                  disabledforeground="black")
    state.place(x=X_REF + 270, y=Y_REF + 300 + 25, width=150, height=25)

    #####
    Label(frame, text='KYC Document', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF, y=Y_REF + 360,
                                                                                           width=100,
                                                                                           height=25)
    kyc = Combobox(frame, width=27, textvariable=kyc, state="readonly", font=font)
    kyc['values'] = (' Aadhaar Card', ' Passport', ' Driving License')
    kyc["background"] = '#ff0000'
    kyc.place(x=X_REF, y=Y_REF + 360 + 25, width=150, height=25)

    def file():
        filename = filedialog.askopenfile(initialdir="/", title='Select a file', filetypes=(('PDF files', '*.pdf'),))
        print(filename.name)

    upload = Button(frame, text='Upload', bd=1, relief=SOLID, command=file)
    upload.place(x=X_REF + 160, y=Y_REF + 360 + 25, width=50, height=25)

    #####
    Label(frame, text='Reference No.', font=font, bg=color_bg, anchor='w', fg='grey').place(x=X_REF + 240,
                                                                                            y=Y_REF + 360,
                                                                                            width=180, height=25)
    state = Entry(frame, bd=1, relief=SOLID, font=font, state=DISABLED, disabledbackground="white",
                  disabledforeground="black")
    state.place(x=X_REF + 240, y=Y_REF + 360 + 25, width=180, height=25)
