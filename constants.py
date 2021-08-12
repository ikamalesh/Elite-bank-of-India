from time import sleep
from pathlib import Path
from tkinter.ttk import Progressbar, Style, Combobox
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import json
import pyrebase
import csv

button_list = {}

ASSETS_PATH = Path(__file__).resolve().parent / "assets"

w = 900
h = 600
color_bg = 'white'
color_logogreen = '#175C4C'
color_orange = '#F29765'
color_darkblack = '#232425'
color_topbar = '#9FD1C2'


def logo(width, file):
    global logo_img
    logo_img = Image.open(ASSETS_PATH / f"2/{file}")
    logo_img = logo_img.resize((width, width))
    logo_img = ImageTk.PhotoImage(logo_img)
    return logo_img


def progress_bar(frame):
    #style = Style()
    #style.theme_use('alt')
    #style.configure("Horizontal.TProgressbar", background=color_logogreen)

    progress = Progressbar(frame, orient=HORIZONTAL,
                           length=300, mode='determinate', style="green.Horizontal.TProgressbar")
    progress.place(x=w / 2 - 150, y=400, height=15)
    bar_position = 0

    for i in range(0, 105):
        progress['value'] = bar_position
        progress.update()
        bar_position = i
        sleep(0.05)


def topbar(frame, contents):
    top_bar = Frame(frame, bg=color_topbar)
    top_bar.place(x=0, y=0, width=w, height=30)
    x_ref = 10
    for items in contents:
        b = Button(frame, text=items, command=contents[items], bg=color_topbar, activebackground=color_topbar,
                   font=("Lato", 10,), bd=0, relief=SOLID)
        b.place(x=x_ref, y=0, width=50, height=30)
        x_ref += 60


def sidebar(frame, contents):
    y_ref = 1
    for items in contents:
        b = Button(frame, text=items, command=contents[items], bg=color_topbar, activebackground=color_topbar,
                   font=("Lato", 13,), bd=0, relief=SOLID, anchor='w')
        b.place(x=0, y=y_ref, width=250, height=35)
        y_ref += 36
        button_list[items] = b


def all_normal(button_list):
    for button in list(button_list.values()):
        button.config(bg=color_topbar)

