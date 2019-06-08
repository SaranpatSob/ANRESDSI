from firebase import firebase

firebase = firebase.FirebaseApplication('https://test-database-anres.firebaseio.com', None)


while True:
    a = firebase.get('/phishing_data',None)
    print(len(a))
    if(len(a) == 0 or a is None):
        break
    try:
        firebase.delete('/phishing_data',None)
    except:
        continue