import pyrebase
import random
import datetime
import os

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
while True:
    ini_cmd = int(input('''1 . New Account
2 . Login
3 . Exit 
    
>>> '''))

    if ini_cmd == 1:
        print('***** NEW USER REGISTRATION *****')
        name = input('Full name >>> ').title()
        age = input('Age >>> ')
        gender = input('Gender >>> ')
        address = input('Residential address >>> ')
        phone = int(input('Phone >>> '))
        email_number = str(input('Email >>> '))
        email_dot = email_number.replace('.', '<dot>')
        password = input('New Password >>> ')
        account_number = random.randint(10001, 99999)
        data = {'name': name, 'age': age, 'gender': gender, 'address': address, 'phone': phone, 'email': email_number,
                'password': password, 'balance': 0, 'account_number': account_number}

        if str(db.child('users').child(email_dot).get().val()) == 'None':
            db.child('users').child(email_dot).set(data)
            db.child('map').child(account_number).set(email_dot)
        else:
            print('User already exists')


    def after_login(dictionary):
        while True:
            user_input = int(input('''
            1 . Check Balance
            2 . Deposit
            3 . Withdraw
            4 . View Transactions
            5 . Online Transfer
            6 . Exit
            >>> '''))

            if user_input == 1:
                print(f"Your Balance = {dictionary['balance']}")
            elif user_input == 2:
                deposit_amt = int(input('Deposit amount >>> '))
                new_bal = int(dictionary['balance']) + deposit_amt
                db.child('users').child(email_dot).update({'balance': new_bal})
            elif user_input == 3:
                withdraw_amt = int(input('Withdraw amount >>> '))
                new_bal = int(dictionary['balance']) - withdraw_amt
                db.child('users').child(email_dot).update({'balance': new_bal})
            elif user_input == 4:
                v = db.child('users').child(email_dot).child('transactions').get().each()
                for items in v:
                    print(items.val())
            elif user_input == 5:
                to = int(input('Transfer to? >>> '))
                to_email = db.child('map').child(to).get().val()
                amount = int(input('Transfer amount >>> '))

                #sender side
                sender_amt = int(dictionary['balance']) - amount

                #receiverside
                receiver_amt = int(dict(db.child('users').child(to_email).get().val())['balance']) + amount

                now = datetime.datetime.now()
                now = now.strftime('%d/%m/%Y %H:%M%p')
                acc_no = dictionary['account_number']
                ref_code = f"REF{random.randint(101,999)}{random.choice(['aPl','bQd','cYg','eFd','eLG','ATe','BSf','GPy','TWr','JMu','PdR'])}"

                db.child('users').child(to_email).update({'balance': receiver_amt})
                db.child('users').child(to_email).child('transactions').push(f"{now} {ref_code} {f'Rs.{amount} CREDIT':>17} - {f'Acc No.{acc_no}': <5}")

                db.child('users').child(email_dot).update({'balance': sender_amt})
                db.child('users').child(email_dot).child('transactions').push(f"{now} {ref_code} {f'Rs.{amount} DEBIT':>17} - {f'Acc No.{to}': <5}")

            elif user_input == 6:
                break
            dictionary = dict(db.child('users').child(email_dot).get().val())


    if ini_cmd == 2:

        print('***** USER LOGIN *****')

        email_number = input('Email/ Account number >>> ')
        password = input('New Password >>> ')

        try:
            email_number = int(email_number)
            v0 = db.child('map').child(email_number).get().val()
            email_dot = v0
            v = dict(db.child('users').child(v0).get().val())
            if password == v['password']:
                after_login(v)
            else:
                print('Wrong password')

        except ValueError:
            email_number = email_number.replace('.', '<dot>')
            email_dot = email_number
            v = dict(db.child('users').child(email_number).get().val())
            if password == v['password']:
                after_login(v)
            else:
                print('Wrong password')

    if ini_cmd ==3:
        exit()
    os.system('cls')

