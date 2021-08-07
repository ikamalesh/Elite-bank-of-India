import json
import pyrebase

with open('assets/firebase.json', 'r') as c:
    firebaseConfig = json.load(c)
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()

def signup(firstname, lastname, dob, gender, address, district, state, pincode, nationality, mobile, email, kyc_type,
           kyc_ref, kyc_upload, account_type):
    data = {
        "firstname":firstname,
        "lastname":lastname,
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
        "kyc_upload":kyc_upload,
        "account_type":account_type
    }
    db.child('user_requests').set(data)
