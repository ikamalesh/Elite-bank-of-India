import pyrebase

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

data = {'35712': 'srikamalesh<dot>2001@gmail<dot>com'}
#v = db.child('map').set(data)

account = input('>>> ')
try:
    account = int(account)
    v0 = db.child('map').child(account).get().val()
    v = dict(db.child('users').child(v0).get().val())
    print(v)

except ValueError:
    account = account.replace('.','<dot>')
    v = dict(db.child('users').child(account).get().val())
    print(v)
