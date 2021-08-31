import operations
from Application import *


def newaccount_contents(frame):
    global img2, imglabel2
    img2 = logo(width=200, height=100, file='bestbanks1.png', resize=True)
    imglabel2 = Label(frame, image=img2, bd=0, bg=color_bg)
    imglabel2.place(x=10, y=30)

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

    topbar_contents = {'< Back': frame.destroy, }
    topbar(frame, topbar_contents)

    X_REF = 80
    X_REF2 = 600
    Y_REF = 170
    font = ("Lato", 10)

    global gender, accounttype
    accounttype = StringVar(value='Savings')
    gender = StringVar(value='None')



    ######LABELS
    l_title = Label(frame, text='Title', font=font, bg=color_bg, anchor='w', fg='grey')
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

    l_title_n = Label(frame, text='Title', font=font, bg=color_bg, anchor='w', fg='grey')
    l_firstname_n = Label(frame, text='Nominee First name', font=font, bg=color_bg, anchor='w', fg='grey')
    l_lastname_n = Label(frame, text='Nominee Last name', font=font, bg=color_bg, anchor='w', fg='grey')
    l_mobile_n = Label(frame, text='Nominee Mobile number', font=font, bg=color_bg, anchor='w', fg='grey')
    l_email_n = Label(frame, text='Nominee Email', font=font, bg=color_bg, anchor='w', fg='grey')
    l_relationship_n = Label(frame, text='Relationship', font=font, bg=color_bg, anchor='w', fg='grey')

    ######LABELS PLACE
    l_title.place(x=X_REF, y=Y_REF, width=100, height=25)
    l_firstname.place(x=X_REF + 90, y=Y_REF, width=100, height=25)
    l_lastname.place(x=X_REF + 260, y=Y_REF, width=100, height=25)
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

    l_title_n.place(x=X_REF2, y=Y_REF, width=100, height=25)
    l_firstname_n.place(x=X_REF2 + 90, y=Y_REF, width=120, height=25)
    l_lastname_n.place(x=X_REF2 + 260, y=Y_REF, width=120, height=25)
    l_mobile_n.place(x=X_REF2, y=Y_REF + 60, width=150, height=25)
    l_email_n.place(x=X_REF2 + 220, y=Y_REF + 60, width=100, height=25)
    l_relationship_n.place(x=X_REF2 , y=Y_REF + 120, width=100, height=25)

    ######ENTRIES
    title = Combobox(frame, state="readonly", font=font)
    title['values'] = (' Mr', ' Mrs', ' Miss', ' Ms')
    title["background"] = '#ff0000'
    firstname = Entry(frame, bd=1, relief=SOLID, font=font)
    lastname = Entry(frame, bd=1, relief=SOLID, font=font)
    dob = Entry(frame, bd=1, relief=SOLID, font=font)
    acctype1 = Radiobutton(frame, text='Savings', variable=accounttype, font=font, bg=color_bg, value='Savings',
                           activebackground=color_bg, anchor='w')
    acctype2 = Radiobutton(frame, text='Current', variable=accounttype, font=font, bg=color_bg, value='Current',
                           activebackground=color_bg)
    mobile = Entry(frame, bd=1, relief=SOLID, font=font)
    email = Entry(frame, bd=1, relief=SOLID, font=font)
    gender1 = Radiobutton(frame, text='Male', variable=gender, font=font, bg=color_bg, value='Male',
                          activebackground=color_bg, anchor='w')
    gender2 = Radiobutton(frame, text='Female', variable=gender, font=font, bg=color_bg, value='Female',
                          activebackground=color_bg)
    nation = Combobox(frame, width=27, state="readonly", font=font)
    nation['values'] = (' India', ' Sri Lanka', ' Bangladesh')
    nation["background"] = '#ff0000'
    address = Entry(frame, bd=1, relief=SOLID, font=font)
    pincode = Entry(frame, bd=1, relief=SOLID, font=font)
    pincode.bind("<FocusOut>", pincode_event)
    district = Entry(frame, bd=1, relief=SOLID, font=font, state=DISABLED, disabledbackground="white",disabledforeground="black")
    state = Entry(frame, bd=1, relief=SOLID, font=font, state=DISABLED, disabledbackground="white",disabledforeground="black")
    kyc_combo = Combobox(frame, width=27, state="readonly", font=font)
    kyc_combo['values'] = (' PAN Card', ' Aadhaar Card', ' Passport')
    kyc_combo["background"] = '#ff0000'
    refno = Entry(frame, bd=1, relief=SOLID, font=font, disabledbackground="white",disabledforeground="black")

    title_n = Combobox(frame, state="readonly", font=font)
    title_n['values'] = (' Mr', ' Mrs', ' Miss', ' Ms')
    title_n["background"] = '#ff0000'
    firstname_n = Entry(frame, bd=1, relief=SOLID, font=font)
    lastname_n = Entry(frame, bd=1, relief=SOLID, font=font)
    mobile_n = Entry(frame, bd=1, relief=SOLID, font=font)
    email_n = Entry(frame, bd=1, relief=SOLID, font=font)
    relationship = Combobox(frame, state="readonly", font=font)
    relationship['values'] = (' Father', ' Mother', ' Friend', ' Family')
    relationship["background"] = '#ff0000'

    ######ENTRIES PLACE
    title.place(x=X_REF, y=Y_REF + 25, height=23, width=70)
    firstname.place(x=X_REF + 90, y=Y_REF + 25, width=150, height=23)
    lastname.place(x=X_REF + 90+170, y=Y_REF + 25, width=150, height=23)
    dob.place(x=X_REF, y=Y_REF + 60 + 25, width=150, height=23)
    acctype1.place(x=X_REF + 220, y=Y_REF + 60 + 25, width=100, height=25)
    acctype2.place(x=X_REF + 320,y=Y_REF + 60 + 25, width=100,height=25)
    mobile.place(x=X_REF, y=Y_REF + 120 + 25, width=200, height=23)
    email.place(x=X_REF + 220, y=Y_REF + 120 + 25, width=200, height=23)
    gender1.place(x=X_REF, y=Y_REF + 180 + 25, width=100, height=25)
    gender2.place(x=X_REF + 100, y=Y_REF + 180 + 25,width=100, height=25)
    nation.place(x=X_REF + 220, y=Y_REF + 180 + 25, width=200, height=23)
    address.place(x=X_REF, y=Y_REF + 240 + 25, width=420, height=23)
    pincode.place(x=X_REF, y=Y_REF + 300 + 25, width=100, height=23)
    district.place(x=X_REF + 110, y=Y_REF + 300 + 25, width=150, height=23)
    state.place(x=X_REF + 270, y=Y_REF + 300 + 25, width=150, height=23)
    kyc_combo.place(x=X_REF, y=Y_REF + 360 + 25, width=150, height=23)
    refno.place(x=X_REF + 240, y=Y_REF + 360 + 25, width=180, height=23)
    upload = Button(frame, text='Upload', bd=1, relief=SOLID, command=file)
    upload.place(x=X_REF + 160, y=Y_REF + 360 + 25, width=50, height=23)

    title_n.place(x=X_REF2, y=Y_REF + 25, height=23, width=70)
    firstname_n.place(x=X_REF2 + 90, y=Y_REF + 25, width=150, height=23)
    lastname_n.place(x=X_REF2 + 90 + 170, y=Y_REF + 25, width=150, height=23)
    mobile_n.place(x=X_REF2, y=Y_REF + 60 + 25, width=200, height=23)
    email_n.place(x=X_REF2 + 220, y=Y_REF + 60 + 25, width=200, height=23)
    relationship.place(x=X_REF2, y=Y_REF + 25+ 120, height=23, width=100)



    l_captcha_n = Label(frame, text='Enter the shown text', font=font, bg=color_bg, anchor='w', fg='grey')
    l_captcha_n.place(x=X_REF2+149, y=Y_REF+180, width=145, height=25)

    global bg_display, bg_img
    bg_img = logo(300, height=300, file='background.png',resize=False)

    bg_display = Label(frame,image=bg_img, bg=color_bg, bd=0, relief=SOLID,)
    bg_display.place(x=X_REF2, y=Y_REF + 205, width=150, height=30)

    captcha_display = Label(frame, text='', font=('times', 20),bg='#CBCBCB',bd=0,relief=SOLID,)
    captcha_display.place(x=X_REF2+25, y=Y_REF+205, width=100,height=30)

    captcha_entry = Entry(frame, bg=color_bg, bd=1,relief=SOLID, font=('times', 20),justify=CENTER )
    captcha_entry.place(x=X_REF2+149, y=Y_REF+205, width=150,height=30)

    captcha_refresh = Button(frame, text='↻', bd=0, relief=SOLID, command=lambda: change_captcha(captcha_display,captcha_entry), font=('times', 15),bg=color_bg,activebackground=color_bg,fg='red')
    captcha_refresh.place(x=X_REF2 + 301, y=Y_REF + 205, width=20, height=20)

    change_captcha(captcha_display,captcha_entry)

    button_signup = Button(frame, bd=0, text='Sign up', bg='#B3E982', fg='#283556', activebackground='#BCEC91',
                          activeforeground='#283556', font=("Lato", 10, 'bold'), cursor='hand2', command=check_captcha)
    button_signup.place(x=X_REF2+50, y=Y_REF + 360+21, width=250, height=27)

    l_otp_n = Label(frame, text='One time password', font=font, bg=color_bg, anchor='w', fg='grey')
    l_otp_n.place(x=X_REF2, y=Y_REF + 250, width=145, height=25)

    otp_entry = Entry(frame, bg=color_bg, bd=1, relief=SOLID, font=('times', 20), justify=CENTER)
    otp_entry.place(x=X_REF2 , y=Y_REF + 275, width=150, height=30)

    def otp():
        otp_resend.place(x=X_REF2 + 151, y=Y_REF + 275, width=20, height=20)
        from threading import Thread
        Thread(target=timer).start()
        otp_send.destroy()

    def timer():
        otp_resend.config(state=DISABLED)
        for i in reversed(range(120)):
            timer_label.config(text=f'Resend OTP in {i} seconds.')
            sleep(1)
            timer_label.update()
        timer_label.config(text='')
        otp_resend.config(state=NORMAL)


    otp_send = Button(frame, text='Send OTP',bd=1,relief=SOLID,font=('lato',11),bg=color_bg,command=otp,activebackground=color_bg)
    otp_send.place(x=X_REF2 , y=Y_REF + 275, width=150, height=30)

    otp_resend = Button(frame, text='↻', bd=0, relief=SOLID, font=('times', 15), bg=color_bg, activebackground=color_bg, fg='red',command=otp)

    timer_label = Label(frame, text='',bg=color_bg,fg='red')
    timer_label.place(x=X_REF2 + 171, y=Y_REF + 275, width=200, height=20)

    agree_termsandconditions = Checkbutton(frame, text = "I agree to the terms and conditions", onvalue = 1, offvalue = 0, height=5, width = 20,bg=color_bg,activebackground=color_bg)
    agree_termsandconditions.place(x=X_REF2, y=Y_REF + 325, width=200, height=20)