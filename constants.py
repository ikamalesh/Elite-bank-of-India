from time import sleep
from pathlib import Path
from tkinter.ttk import Progressbar, Style
from tkinter import *
from PIL import Image, ImageTk

ASSETS_PATH = Path(__file__).resolve().parent / "assets"


w = 900
h = 600
color_bg = '#EDF1F4'
color_logogreen = '#175C4C'
color_orange = '#F29765'
color_darkblack = '#232425'
color_topbar = '#9FD1C2'


def logo(width,file):
    global logo_img
    logo_img = Image.open(ASSETS_PATH / f"2/{file}")
    logo_img = logo_img.resize((width, width))
    logo_img = ImageTk.PhotoImage(logo_img)
    return logo_img

def progress_bar(frame):
    style = Style()
    style.theme_use('alt')
    style.configure("green.Horizontal.TProgressbar", background=color_logogreen)

    progress = Progressbar(frame, orient=HORIZONTAL,
                           length=300, mode='determinate', style="green.Horizontal.TProgressbar")
    progress.place(x=w / 2 - 150, y=400, height=15)
    bar_position = 0

    for i in range(0, 105):
        progress['value'] = bar_position
        progress.update()
        bar_position = i
        sleep(0.05)
