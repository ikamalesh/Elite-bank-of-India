

def send(otp,number):
    import webbrowser    
    urL='https://www.google.com'
    chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),)
    webbrowser.get('chrome').open_new_tab(f"https://api.whatsapp.com/send?phone=91{number}&text=Dear Customer, One Time Password (OTP) to access is *{otp}* . AIRFIBER never calls to verify OTP. Do not disclose OTP to anyone.")

send(1230,8667224209)