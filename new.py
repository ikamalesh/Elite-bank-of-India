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

def sample1():
    email = input('>>> ').replace('.', '<dot>')

    v = db.child('users').child(email).child('transactions').get().each()
    for items in v:
        print(items.val())

    import datetime


    amount = 254
    dictionary = {'account_number': 15478}
    import datetime
    now = datetime.datetime.now()
    now = now.strftime('%d/%m/%Y %H:%M%p')

    final = f"{now} {f'Rs.{amount} CREDIT':<20} - Acc No.{dictionary['account_number']}"

    print(final)


data = {'title': 'update 2', "body": "Updated body 2"}
db.child('messages').push(data)