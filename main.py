import json
from pathlib import Path
from tkinter import *
import pyrebase
import second_page


# Path to asset files for this GUI window.
ASSETS_PATH = Path(__file__).resolve().parent / "assets"

with open('assets/firebase.json', 'r') as c:
    firebaseConfig = json.load(c)
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()

def window_sam():
    window = Tk()

def main_window():
    global w,h
    w, h = 900, 600

    window.geometry(f"{w}x{h}")
    window.title("")

    frame_login = Frame(window, bg='white')
    frame_login.place(x=0,y=0,width=w,height=h)
    Frame(window, bg='grey').place(x=0, y=0, width=w, height=30)

    Button(frame_login, text='Second window', command=second_page.loginpage).place(x=100,y=100)


if __name__ == '__main__':
    global window
    window_sam()
    main_window()
    window.mainloop()