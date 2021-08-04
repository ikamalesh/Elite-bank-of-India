import json
import pyrebase
from constants import *
from windows import *

# Path to asset files for this GUI window.
ASSETS_PATH = Path(__file__).resolve().parent / "assets"

def firebase():
    with open('assets/firebase.json', 'r') as c:
        firebaseConfig = json.load(c)
    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    auth = firebase.auth()


class Interface():
    def __init__(self, window):
        window.title("Rossum's Bank")
        global logo_label
        frame_starter = Frame(window, bg=color_darkblack)
        frame_starter.place(x=0, y=0, width=w, height=h)
        logo_img = logo()
        logo_label = Label(frame_starter, image=logo_img, bd=0, bg=color_darkblack)
        logo_label.place(x=w / 2 - 300 / 2, y=h / 2 - 300 / 2)
        #progress_bar(frame_starter)
        frame_starter.destroy()
        Interface.login_window()

    def login_window():
        frame_login = Frame(window, bg='white')
        frame_login.place(x=0, y=0, width=w, height=h)
        login_contents(frame=frame_login)

    def about():
        print('in about page')

    def home():
        print('in home page')


if __name__ == '__main__':
    window = Tk()
    window.geometry(f"{w}x{h}")
    app = Interface(window)
    window.mainloop()
