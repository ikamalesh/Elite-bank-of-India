from constants import *
import main


def topbar(frame, contents):
    top_bar = Frame(frame, bg='grey')
    top_bar.place(x=0, y=0, width=w, height=30)
    x_ref = 0

    for items in contents:
        b = Button(frame, text=items, bd=0, command=contents[items], bg=color_orange)
        b.place(x=x_ref, y=0, width=100, height=30)
        x_ref += 100


def login_contents(frame):
    topbar_contents = {'About': main.Interface.about,
                       'Home': main.Interface.home}
    Label(frame, text='Email or Account Number', anchor='w', bg=color_white).place(x=w / 2 - 300 / 2, y=200, width=300, height=20)
    Label(frame, text='Password', anchor='w', bg=color_white).place(x=w / 2 - 300 / 2, y=250, width=300, height=20)

    topbar(frame, topbar_contents)
