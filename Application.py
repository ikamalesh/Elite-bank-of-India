import Contents_1
import Contents_2
from CONST import *
import operations

# Path to asset files for this GUI window.
ASSETS_PATH = Path(__file__).resolve().parent / "assets"


class App():    
    def __init__(self, window):
        window.title("Elite Bank of India")
        global logo_label, logo_img
        frame_starter = Frame(window, bg=color_bg)
        frame_starter.place(x=0, y=0, width=w, height=h)
        logo_img = logo(300, height=300, file='wholecrop.png')
        logo_label = Label(frame_starter, image=logo_img, bd=0, bg=color_bg)
        logo_label.place(x=w / 2 - 250, y= 160)
        #progress_bar(frame_starter)
        frame_starter.destroy()
        data = dict(operations.db.child('active_users').child('HB23961').get().val()) #Hack
        #App.login_window(window)
        App.main_window(window, data)


    def login_window(self):
        frame_login = Frame(self, bg=color_bg)
        frame_login.place(x=0, y=0, width=w, height=h)
        Contents_1.login_contents(frame=window)
        Contents_1.login_contents(frame=window)

    def newaccount_window(self):
        self.title("Elite Bank of India | New Account")
        frame_new = Frame(self, bg=color_bg)
        frame_new.place(x=0, y=0, width=w, height=h)
        Contents_2.newaccount_contents(frame=frame_new)

    def about():
        print('in about page')

    def home():
        print('in home page')

    def profile(self, data):
        all_normal(button_list)
        button_list[' Profile'].config(bg=color_bg, fg='#202225')

        frame1 = Frame(self, bg=color_bg, bd=0)
        frame1.place(x=230 + 0, y=30, width=w - 230, height=h - 30)

        global profile_label, profile_img
        profile_img = logo(width=150, height=150, file=f'{data["gender"]}.png', resize=True)
        profile_label = Label(frame1, image=profile_img, bd=0, bg=color_bg)
        profile_label.place(x=(w - 230) / 2 - (150 / 2), y=h / 2 - 250)

        name_label = Label(frame1, text=data['firstname'], font=('lato', 25, "bold"), bg=color_bg, fg='#202225', )
        name_label.place(width=400, height=50, x=(w - 230) / 2 - (400 / 2), y=h / 2 - 80)

        email_label = Label(frame1, text=f"{data['email']}", font=('lato', 13,), bg=color_bg, fg='#202225', )
        email_label.place(width=300, x=(w - 230) / 2 - (300 / 2), y=h / 2 - 25)

        accno_label = Label(frame1, text=f"Account No: {data['account_number']}", font=('lato', 13,), bg=color_bg,
                            fg='#202225', )
        accno_label.place(width=200, x=(w - 230) / 2 - (200 / 2), y=h / 2)

        edit_profile = Button(frame1, text='Edit profile', font=("lato", 9), bg=color_bg, bd=0, fg='blue',
                              activebackground=color_bg)
        edit_profile.place(width=70, height=25, x=((w - 230) / 2) - 70 / 2, y=h / 2 + 25, )

    def check_balance(self, position):
        all_normal(button_list)
        button_list[' Check Balance'].config(bg=color_bg, fg='#202225')

        frame2 = Frame(self, bg=color_bg, bd=0)
        frame2.place(x=230, y=30, width=w - 230, height=h - 30)

        Label(frame2, text='In frame 2').pack()

    def view_transactions():
        all_normal(button_list)
        button_list[' View Transactions'].config(bg=color_bg, fg='#202225')

    def online_transfer():
        all_normal(button_list)
        button_list[' Online Transfer'].config(bg=color_bg, fg='#202225')

    def deposit():
        all_normal(button_list)
        button_list[' Deposit'].config(bg=color_bg, fg='#202225')

    def withdraw():
        all_normal(button_list)
        button_list[' Withdraw'].config(bg=color_bg, fg='#202225')

    def investments():
        all_normal(button_list)
        button_list[' Investments'].config(bg=color_bg, fg='#202225')

    def personal_loans():
        all_normal(button_list)
        button_list[' Personal Loans'].config(bg=color_bg, fg='#202225')

    def main_window(self, data):
        frame_main = Frame(self, bg=color_bg)
        frame_main.place(x=0, y=0, width=w, height=h)

        frame_right = Frame(self, bg=color_bg, bd=0, relief=GROOVE)
        # frame_right.place(x=230, y=30, width=w - 230, height=h - 30)

        frame_left = Frame(self, bg='#202225', bd=0)  # bg=color_logogreen)
        frame_left.place(x=0, y=120, width=230, height=h - 120)

        Contents_1.main_contents(frame=frame_main, framel=frame_left, data=data)


if __name__ == '__main__':
    window = Tk()
    window.geometry(f"{w}x{h}+10+10")
    window.resizable(0, 0)
    App(window)
    window.mainloop()
