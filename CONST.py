import random
from assets import mailer
from time import sleep, strftime
from pathlib import Path
from tkinter.ttk import Progressbar, Style, Combobox
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import json
import pyrebase
import csv
from threading import Thread



button_list = {}

ASSETS_PATH = Path(__file__).resolve().parent / "assets"

w = 1100
h = 700

color_bg = 'white'
color_logogreen = '#175C4C'
color_orange = '#F29765'
color_darkblack = '#232425'
color_topbar = "#202225"  # '#5A86BF'
##202225 dark

def logo(width, height, file, resize=False):
    global logo_img
    logo_img = Image.open(ASSETS_PATH / f"{file}")
    if resize == True:
        logo_img = logo_img.resize((width, height))
    else:
        pass
    logo_img = ImageTk.PhotoImage(logo_img)
    return logo_img


def progress_bar(frame):
    # style = Style()
    # style.theme_use('alt')
    # style.configure("Horizontal.TProgressbar", background=color_logogreen)

    progress = Progressbar(frame, orient=HORIZONTAL,
                           length=300, mode='determinate', style="green.Horizontal.TProgressbar")
    progress.place(x=w / 2 - 150, y=440, height=15)
    bar_position = 0

    for i in range(0, 105):
        progress['value'] = bar_position
        progress.update()
        bar_position = i
        sleep(0.05)


def topbar(frame, contents):
    top_bar = Frame(frame, bg=color_topbar, bd=0)
    top_bar.place(x=0, y=0, width=w, height=30)

    x_ref = 10
    for items in contents:
        b = Button(frame, text=items, command=contents[items], bg=color_topbar, activebackground=color_topbar,
                   font=("Lato", 10,), bd=0, relief=SOLID, fg='white',activeforeground='white')  # cursor='hand2',
        b.place(x=x_ref, y=0, width=50, height=30)

        x_ref += 60


def sidebar(frame, contents):
    y_ref = 1
    for items in contents:
        b = Button(frame, text=items, command=contents[items], bg=color_topbar, activebackground=color_topbar,
                   fg='white',
                   font=("Lato", 13,), bd=0, relief=SOLID, anchor='w', cursor='hand2', activeforeground='white')
        b.place(x=0, y=y_ref, width=250, height=35)
        y_ref += 35
        button_list[items] = b


def all_normal(button_list):
    for button in list(button_list.values()):
        button.config(bg=color_topbar, fg='white')


capcha_list = ['598W', 'Tesj', 'vvGj', 'YJLN', 'C1YK', 'TlOo', 'PNg4', 'j5uI', 'gvuP', '1UtL', '3uUI', 'EOFD',
               'vWJ6', '5jjk', 'kRVE', 'togd', 'iRSV', 'WZCI', 'L5mB', 'PrbD', 'feIk', 'A3n2', 'pGAi', 'OCj4', 'Yunh',
               'QGTD',
               'W8RZ', 'iJGV', '9eQc', '3Zwr', 'dRux', '0hjm', 'CY0H', 'U2o9', 'PuAS', 'MhKB', 'k1zC', 'uFP3', 'hLcD',
               'Qq09',
               '3sdW', 'lyfp', 'fZ80', 'heLK', '0axD', 'B399', 'X0rv', '8tGy', 'PvRh', '2fwH', 'JDXH', 'aqHx', 'u9VB',
               'kBK1',
               '0noL', '5qvE', 'tEp7', 'lNue', 'FxWL', 'dM2d', 'vqhH', 'hI80', 'Bs9a', 'Wvbj', 'L0AH', 'XQx5', 'HRuA',
               'vuS1',
               'j2ON', 'LfkQ', 'JLsx', 'BikD', 'olfY', '0Y1V', 'm9it', '5Y7w', 'sklx', 'TzjH', 'Ixl6', 'XcPs', 'mhEl',
               'e0LX',
               'j9oX', '0qIp', 'UU0I', 'nd49', 'bSeY', 'HL9k', 'kp1V', 'tz3C', 'osak', 'WOF3', 'mat5', 'pggb', 'Znwo',
               'MH1A',
               'uIFN', 'Feyi', 'KX1i', '4iO9', 'Ad3s']


def change_captcha(label, entry):
    entry.delete(0, END)
    global captcha_text
    p = random.choice(capcha_list)
    label.config(text=p)
    captcha_text = p

def check_captcha(captcha_entry):
    global captcha_text
    if str(captcha_entry) == str(captcha_text):
        return True
    else:
        return False

def check_mobilenumber(number):
    if len(number) == 10:
        try:
            number = int(number)
            return True
        except:
            return False
    else:
        return False

def check_email(email):
    if email == '':
        print('ntg')
    else:
        if '@' in email or '.com' in email or '.co.in' in email:
            return True
        else:
            return False

def check_dob(dob_entry):
    dob = dob_entry.split('/')
    #['11', '04', '2001']

    if len(dob[0]) == 2 and len(dob[1])==2 and len(dob[2])==4:
        try:
            day = int(dob[0])
            month= int(dob[1])
            year= int(dob[2])
            if day <=31:
                if month <=12:
                    if year < 2003:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        except:
            return False
    else:
        return False

def send_otp(emailid,otp):
    mailer.send(emailid,'Verification',f'Your OTP - {otp}')
