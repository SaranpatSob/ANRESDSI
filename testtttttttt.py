from firebase import firebase

firebase = firebase.FirebaseApplication('https://test-database-anres.firebaseio.com', None)

inp = int(input())

result = firebase.get('/phishing_data','mycrosoft_com')

print(result)