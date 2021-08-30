import operations
from Application import *

def newaccount_contents(frame):
    global smile_img1, smile_label1
    smile_img1 = logo(64,64, file='smile.png')
    smile_label1 = Label(frame, image=smile_img1, bd=0, bg=color_bg)
    smile_label1.place(x=20, y=h - 70)

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
        filename = filedialog.askopenfile(initialdir="/", title='Select a file', filetypes=(('All files', '*.*'),
                                                                                            ('PDF files', '*.pdf'),
                                                                                            ('JPG files', '*.jpg'),
                                                                                            ('JPEG files', '*.jpeg')))
        try:
            flename = filename.name
        except:
            pass

    def submit_button():
        operations.signup(l_error,
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

    topbar_contents = {'< Back': frame.destroy, }
    topbar(frame, topbar_contents)

    X_REF = 50
    Y_REF = 70
    font = ("Lato", 10)

    accounttype = StringVar(value='Savings')
    gender = StringVar(value='None')
    nationality = StringVar()
    kyc = StringVar()

    ######LABELS
    l_title =  Label(frame, text='Title', font=font, bg=color_bg, anchor='w', fg='grey')
    l_firstname = Label(frame, text='First name', font=font, bg=color_bg, anchor='w', fg='grey')
    l_lastname = Label(frame, text='Last name', font=font, bg=color_bg, anchor='w', fg='grey')
    l_dob = Label(frame, text='DOB (DD/MM/YYYY)', font=font, bg=color_bg, anchor='w', fg='grey')
    l_acctype = Label(frame, text='Account type', font=font, bg=color_bg, anchor='w', fg='grey', )
    l_mobile = Label(frame, text='Mobile number', font=font, bg=color_bg, anchor='w', fg='grey')
    l_email = Label(frame, text='Email', font=font, bg=color_bg, anchor='w', fg='grey')
    l_gender = Label(frame, text='Gender', font=font, bg=color_bg, anchor='w', fg='grey')
    l_nationality = Label(frame, text='Nationality', font=font, bg=color_bg, anchor='w', fg='grey')
    l_address = Label(frame, text='Address', font=font, bg=color_bg, anchor='w', fg='grey')
    l_pincode = Label(frame, text='Pincode', font=font, bg=color_bg, anchor='w', fg='grey')
    l_district = Label(frame, text='District', font=font, bg=color_bg, anchor='w', fg='grey')
    l_state = Label(frame, text='State', font=font, bg=color_bg, anchor='w', fg='grey')
    l_kyc = Label(frame, text='KYC Document', font=font, bg=color_bg, anchor='w', fg='grey')
    l_refno = Label(frame, text='Reference No.', font=font, bg=color_bg, anchor='w', fg='grey')

    ######LABELS PLACE
    l_title.place(x=X_REF, y=Y_REF, width=100, height=25)
    #l_firstname.place(x=X_REF+110, y=Y_REF, width=100, height=25)
    #l_lastname.place(x=X_REF + 220, y=Y_REF, width=100, height=25)
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

    title  = Combobox(frame, state="readonly", font=font)
    title['values'] = (' Mr', ' Mrs', ' Miss', ' Ms')
    title["background"] = '#ff0000'

    #firstname_error = Frame(frame, bg='grey')
    firstname = Entry(frame, bd=1, relief=SOLID, font=font)
    firstname.insert(0, ' First name')

    #lastname_error = Frame(frame, bg='grey')
    lastname = Entry(frame, bd=1, relief=SOLID, font=font)
    lastname.insert(0, ' Last name')


    dob_error = Frame(frame, bg='grey')
    dob = Entry(frame, bd=0, relief=SOLID, font=font)
    dob.bind('<>')


    acctype1 = Radiobutton(frame, text='Savings', variable=accounttype, font=font, bg=color_bg, value='Savings',
                           activebackground=color_bg, anchor='w')
    acctype2 = Radiobutton(frame, text='Current', variable=accounttype, font=font, bg=color_bg, value='Current',
                           activebackground=color_bg)

    mobile_error = Frame(frame, bg='grey')
    mobile = Entry(frame, bd=0, relief=SOLID, font=font)

    email_error = Frame(frame, bg='grey')
    email = Entry(frame, bd=0, relief=SOLID, font=font)

    gender1 = Radiobutton(frame, text='Male', variable=gender, font=font, bg=color_bg, value='Male',
                          activebackground=color_bg, anchor='w')
    gender2 = Radiobutton(frame, text='Female', variable=gender, font=font, bg=color_bg, value='Female',
                          activebackground=color_bg)

    nation = Combobox(frame, width=27, textvariable=nationality, state="readonly", font=font)
    nation['values'] = (' India', ' Sri Lanka', ' Bangladesh')
    nation["background"] = '#ff0000'

    address_error = Frame(frame, bg='grey')
    address = Entry(frame, bd=0, relief=SOLID, font=font)

    pincode_error = Frame(frame, bg='grey')
    pincode = Entry(frame, bd=0, relief=SOLID, font=font)
    pincode.bind("<FocusOut>", pincode_event)

    district_error = Frame(frame, bg='grey')
    district = Entry(frame, bd=0, relief=SOLID, font=font, state=DISABLED, disabledbackground="white",
                     disabledforeground="black")
    state_error = Frame(frame, bg='grey')
    state = Entry(frame, bd=0, relief=SOLID, font=font, state=DISABLED, disabledbackground="white",
                  disabledforeground="black")
    kyc_combo = Combobox(frame, width=27, textvariable=kyc, state="readonly", font=font)
    kyc_combo['values'] = (' PAN Card', ' Aadhaar Card', ' Passport')
    kyc_combo["background"] = '#ff0000'

    refno_error = Frame(frame, bg='grey')
    refno = Entry(frame, bd=0, relief=SOLID, font=font, disabledbackground="white",
                  disabledforeground="black")

    ######ENTRIES PLACE

    title.place(x=X_REF, y=Y_REF + 25, height=23, width=70)

    #firstname_error.place(x=X_REF - 1, y=Y_REF + 25 - 1, width=202, height=25)
    firstname.place(x=X_REF+90, y=Y_REF + 25, width=250, height=23)

    #lastname_error.place(x=X_REF + 220 - 1, y=Y_REF + 25 - 1, width=202, height=25)
    lastname.place(x=X_REF + 360, y=Y_REF + 25, width=250, height=23)

    #dob_error.place(x=X_REF - 1, y=Y_REF + 60 + 25 - 1, width=202, height=25)
    dob.place(x=X_REF, y=Y_REF + 60 + 25, width=200, height=23)


    acctype1.place(x=X_REF + 220, y=Y_REF + 60 + 25, width=100, height=25), acctype2.place(x=X_REF + 320,
                                                                                           y=Y_REF + 60 + 25, width=100,
                                                                                           height=25)

    mobile_error.place(x=X_REF - 1, y=Y_REF + 120 + 25 - 1, width=202, height=25)
    mobile.place(x=X_REF, y=Y_REF + 120 + 25, width=200, height=23)

    email_error.place(x=X_REF + 220 - 1, y=Y_REF + 120 + 25 - 1, width=202, height=25)
    email.place(x=X_REF + 220, y=Y_REF + 120 + 25, width=200, height=23)
    gender1.place(x=X_REF, y=Y_REF + 180 + 25, width=100, height=25), gender2.place(x=X_REF + 100, y=Y_REF + 180 + 25,
                                                                                    width=100, height=25)
    nation.place(x=X_REF + 220, y=Y_REF + 180 + 25, width=200, height=23)

    address_error.place(x=X_REF - 1, y=Y_REF + 240 + 25 - 1, width=422, height=25)
    address.place(x=X_REF, y=Y_REF + 240 + 25, width=420, height=23)

    pincode_error.place(x=X_REF - 1, y=Y_REF + 300 + 25 - 1, width=102, height=25)
    pincode.place(x=X_REF, y=Y_REF + 300 + 25, width=100, height=23)

    district_error.place(x=X_REF + 110 - 1, y=Y_REF + 300 + 25 - 1, width=152, height=25)
    district.place(x=X_REF + 110, y=Y_REF + 300 + 25, width=150, height=23)

    state_error.place(x=X_REF + 270 - 1, y=Y_REF + 300 + 25 - 1, width=152, height=25)
    state.place(x=X_REF + 270, y=Y_REF + 300 + 25, width=150, height=23)

    kyc_combo.place(x=X_REF, y=Y_REF + 360 + 25, width=150, height=23)

    refno_error.place(x=X_REF + 240 - 1, y=Y_REF + 360 + 25 - 1, width=182, height=25)
    refno.place(x=X_REF + 240, y=Y_REF + 360 + 25, width=180, height=23)

    upload = Button(frame, text='Upload', bd=1, relief=SOLID, command=file)
    upload.place(x=X_REF + 160, y=Y_REF + 360 + 25, width=50, height=23)

    ######
    l_error = Label(frame, text="Label error", fg='red', bg=color_bg)
    #l_error.place(x=(w + 30 + 440) / 2 - 250 / 2, y=5, width=250)