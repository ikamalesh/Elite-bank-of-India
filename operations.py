from constants import *
import random

with open('assets/firebase.json', 'r') as c:
    firebaseConfig = json.load(c)
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

def signup(error_tag, firstname, lastname, dob, gender, address, district, state, pincode, nationality, mobile, email, kyc_type,
           kyc_ref, kyc_path, account_type):


    data = {
        "firstname":firstname.title(),
        "lastname":lastname.title(),
        "dob":dob,
        "gender":gender,
        "address":address,
        "district":district,
        "state":state,
        "pincode": pincode,
        "nationality":nationality,
        "mobile":mobile,
        "email":email,
        "kyc_type":kyc_type,
        "kyc_ref":kyc_ref,
        "kyc_upload":kyc_path,
        "account_type":account_type
    }

    combi = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    id = random.choice(combi) + random.choice(combi) + random.choice(combi) + random.choice(combi) + random.choice(combi)
    if db.child('account_requests').child(id).get().val() == None and db.child('account_holders').child(id).get().val()==None:
        db.child('account_requests').child(id).set(data)
        storage.child('account_requests').child(id).put(kyc_path)
        messagebox.showinfo('Account number', f"You Account number: {id}")
    else:
        print('Id Existing')
