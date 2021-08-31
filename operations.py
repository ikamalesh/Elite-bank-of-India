from constants import *
import random
from Application import App

with open('assets/firebase.json', 'r') as c:
    firebaseConfig = json.load(c)
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()


def signup(title, firstname, lastname, dob, account_type, mobile, email, gender, nationality,address, pincode,district, state,
           kyc_type,kyc_ref, kyc_path, nom_title,nom_firstname,nom_lastname,nom_mobile,nom_email,nom_relationship):
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
        "nom_relatinoship":nom_relationship
    }

    combi = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    id = random.choice(combi) + random.choice(combi) + random.choice(combi) + random.choice(combi) + random.choice(
        combi)
    if db.child('account_requests').child(id).get().val() == None and db.child('account_holders').child(
            id).get().val() == None:
        db.child('account_requests').child(id).set(data)
        storage.child('account_requests').child(id).put(kyc_path)
        messagebox.showinfo('Account number', f"You Account number: {id}")
    else:
        print('Id Existing')


def signin(frame, username, password):
    print(username, password)
    try:
        auth.sign_in_with_email_and_password(username, password)
        crt_password = True
        print(crt_password)
    except:
        crt_password = False
        print(crt_password)
