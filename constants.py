from time import sleep
from pathlib import Path
from tkinter.ttk import Progressbar, Style
from tkinter import *
from PIL import Image, ImageTk

ASSETS_PATH = Path(__file__).resolve().parent / "assets"


w = 900
h = 600
color_white = 'white'
color_2 = 'red'
color_orange = '#F29765'
color_darkblack = '#1A1A1A'

def logo():
    global logo_img
    logo_img = Image.open(ASSETS_PATH / "1/Rossum's -logos_white.png")
    logo_img = logo_img.resize((300, 300))
    logo_img = ImageTk.PhotoImage(logo_img)
    return logo_img

def progress_bar(frame):
    style = Style()
    style.theme_use('alt')
    style.configure("green.Horizontal.TProgressbar", background='red')

    progress = Progressbar(frame, orient=HORIZONTAL,
                           length=300, mode='determinate', style="green.Horizontal.TProgressbar")
    progress.place(x=w / 2 - 150, y=500, height=15)
    bar_position = 0

    for i in range(0, 105):
        progress['value'] = bar_position
        progress.update()
        bar_position = i
        sleep(0.05)
