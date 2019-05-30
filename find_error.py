from firebase import firebase

firebase = firebase.FirebaseApplication('https://test-database-anres.firebaseio.com', None)

result = firebase.get('/users', None)

c = 0

# print(result)

for i in result:
    try:
        print(str(c),result[i]['Case'])
        if(c == 0):
            temp = len(i)
        if(len(i) != temp):
            print(i)
        c+=1
    except:
        print(result[i],i)
        firebase.delete('/users',i)
        

#print(result)