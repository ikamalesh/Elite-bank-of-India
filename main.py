import pyrebase
from pathlib import Path
from PIL import Image, ImageTk
import json
from tkinter import *

# Path to asset files for this GUI window.
ASSETS_PATH = Path(__file__).resolve().parent / "assets"

with open('assets/firebase.json', 'r') as c:
    firebaseConfig = json.load(c)
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()

class interface():
    def __init__(self, window):
        width, height=900,600
        window.geometry('900x600')
        window.title('Prezzi Bank')
        frame = Frame(window, bg="#e5cdff")
        frame.place(x=0,y=0,width=width, height=height)

        user_entry = Entry(window, bd=1)
        user_entry.place(width=100, height=25,x=w/2-100/2,y=100)











if __name__ == '__main__':
    window = Tk()
    app = interface(window)
    window.mainloop()