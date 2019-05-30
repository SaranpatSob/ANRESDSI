from firebase import firebase

firebase = firebase.FirebaseApplication('https://test-database-anres.firebaseio.com', None)

result = firebase.get('/users', None)



c = 0

for i in result:
    print(c)
    if(c == 0):
        temp = len(i)
    if(len(i) != temp):
        print(i)
    c+=1

#print(result)