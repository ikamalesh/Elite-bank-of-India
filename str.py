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

def send():
    data = {'title': 'firebase', "body": "Python interface to the Google's Firebase REST APIs"}
    db.child('path').set(data)

def temp():
    def stream_handler(message):
        #v = message['data']
        print(message)

    my_stream = db.child("messages").stream(stream_handler)

def load():
    b = dict(db.child('messages').get().val())
    print(b)

temp()