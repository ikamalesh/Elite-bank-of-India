from constants import *
import contents
import contents2


# Path to asset files for this GUI window.
ASSETS_PATH = Path(__file__).resolve().parent / "assets"


class App():
    def __init__(self, window):
        window.title("Rossum's Bank")
        global logo_label,logo_img
        frame_starter = Frame(window, bg=color_topbar)
        frame_starter.place(x=0, y=0, width=w, height=h)
        logo_img = logo(300, file='white.png')
        logo_label = Label(frame_starter, image=logo_img, bd=0, bg=color_topbar)
        logo_label.place(x=w / 2 - 300 / 2, y=h / 2 - 200)
        #progress_bar(frame_starter)
        frame_starter.destroy()
        App.login_window(window)

    def login_window(self):
        frame_login = Frame(self, bg=color_bg)
        frame_login.place(x=0, y=0, width=w, height=h)
        contents.login_contents(frame=window)
        contents.login_contents(frame=window)

    def newaccount_window(self):
        self.title("Rossum's Bank | New Account")
        frame_new = Frame(self, bg=color_bg)
        frame_new.place(x=0, y=0, width=w, height=h)
        contents2.newaccount_contents(frame=frame_new)

    def about():
        print('in about page')

    def home():
        print('in home page')

    def profile():
        all_normal(button_list)
        button_list[' Profile'].config(bg=color_bg)

    def check_balance():
        all_normal(button_list)
        button_list[' Check Balance'].config(bg=color_bg)

    def view_transactions():
        all_normal(button_list)
        button_list[' View Transactions'].config(bg=color_bg)

    def online_transfer():
        all_normal(button_list)
        button_list[' Online Transfer'].config(bg=color_bg)

    def deposit():
        all_normal(button_list)
        button_list[' Deposit'].config(bg=color_bg)

    def withdraw():
        all_normal(button_list)
        button_list[' Withdraw'].config(bg=color_bg)

    def investments():
        all_normal(button_list)
        button_list[' Investments'].config(bg=color_bg)

    def personal_loans():
        all_normal(button_list)
        button_list[' Personal Loans'].config(bg=color_bg)

    def main_window(self, name):
        frame_main = Frame(self, bg=color_bg)
        frame_main.place(x=0, y=0, width=w, height=h)

        frame_right = Frame(self, bg=color_bg, bd=2, relief=GROOVE)
        frame_right.place(x=230, y=30, width=w - 230, height=h - 30)

        frame_left = Frame(self, bg=color_logogreen)
        frame_left.place(x=0, y=120, width=230, height=h - 120)

        logo_img = logo(90, file='transparent2.png')
        logo_label = Label(frame_main, image=logo_img, bd=0, bg=color_bg)
        logo_label.place(x=0, y=30)

        contents.main_contents(frame=frame_main, frame1=frame_left, frame2=frame_right, name=name)


if __name__ == '__main__':
    window = Tk()
    window.geometry(f"{w}x{h}+10+10")
    window.resizable(0, 0)
    App(window)
    window.mainloop()
