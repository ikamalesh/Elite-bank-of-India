import os

if os.path.exists('assets'):
    if os.path.exists("assets/mailer"):
        print("test pass")
    else:
        print("Mailer module not found")
else:
    print("Assets folder not found")