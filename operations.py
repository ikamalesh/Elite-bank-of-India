import Application
from CONST import *
import random
from Application import App

with open('assets/firebase.json', 'r') as c:
    firebaseConfig = json.load(c)
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()
upload_success = False

def signup(title, firstname, lastname, dob, account_type, mobile, email, gender, nationality,address, pincode,district, state,
           kyc_type,kyc_ref, kyc_path, nom_title,nom_firstname,nom_lastname,nom_mobile,nom_email,nom_relationship):
    global upload_success
    combi = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    id = 'HB' + str(random.randint(11111,99999))

    data = {
        "title": title,
        "firstname": firstname.title(),
        "lastname": lastname.title(),
        "dob": dob,
        "account_type": account_type,
        "mobile": mobile,
        "email": email,
        "gender": gender,
        "nationality": nationality,
        "address": address,
        "pincode": pincode,
        "district": district,
        "state": state,
        "kyc_type": kyc_type,
        "kyc_ref": kyc_ref,
        "kyc_upload": kyc_path,
        "nom_title":nom_title,
        "non_firstname":nom_firstname,
        "nom_lastname":nom_lastname,
        "nom_mobile":nom_mobile,
        "nom_email":nom_email,
        "nom_relatinoship":nom_relationship,
        "balance":0,
        "login_status":False,
        "account_number": id
    }

    if db.child('account_requests').child(id).get().val() == None and db.child('account_holders').child(
            id).get().val() == None:
        db.child('account_requests').child(id).set(data)
        storage.child('documents').child(id).put(kyc_path)
        messagebox.showinfo('Account number', f"You Account number: {id}")
        upload_success = True
    else:
        print('Id Existing')


def signin(frame, accno, password):
    email = db.child('active_users').child(accno).child('email').get().val()
    if email != None:
        try:
           auth.sign_in_with_email_and_password(email, password)
           #data = dict(db.child('active_users').child(accno).get().val())
           #print(data)
           App.main_window(frame,accno=accno)
           print(accno)
        except:
           print('Wrong pass')
    else:
        print('Wrong email')

def profile_datagenerator(accno):
    return dict(db.child('active_users').child(accno).get().val())