import pyrebase
from time import strftime

config = {
    'apiKey': "AIzaSyB2hssgQl3fFauUIPtVGz4mjBiXomia1Tc",
    'authDomain': "pyrebase-realtimedb.firebaseapp.com",
    'databaseURL': "https://pyrebase-realtimedb-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "pyrebase-realtimedb",
    'storageBucket': "pyrebase-realtimedb.appspot.com",
    'messagingSenderId': "729326840647",
    'appId': "1:729326840647:web:edfb9dc037fc352959fa62"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
auth = firebase.auth()

storage = firebase.storage()
user = auth.sign_in_anonymous()
#print(user['idToken'])

account_number = 'HB88334'

fetched_data = dict(db.child('account_requests').child(account_number).get().val())

fetched_data['acc_activated_dt'] = strftime("%Y-%m-%d %H:%M:%S")
print(fetched_data)
db.child('active_users').child(account_number).set(fetched_data)
db.child('account_requests').child(account_number).remove()
