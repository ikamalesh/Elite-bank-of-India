from constants import *

with open('assets/firebase.json', 'r') as c:
    firebaseConfig = json.load(c)
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

def signup(error_tag, firstname, lastname, dob, gender, address, district, state, pincode, nationality, mobile, email, kyc_type,
           kyc_ref, kyc_path, account_type):

    if firstname == '':
        error_tag.config(text='Hello')


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