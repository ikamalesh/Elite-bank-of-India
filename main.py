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

