import pandas as pd 
import numpy as np 
from firebase import firebase

firebase = firebase.FirebaseApplication('https://test-database-anres.firebaseio.com', None)

dt = np.array(pd.read_csv("small.txt"))

data_all = []

for i in dt:
    temp = i[0].split('.')
    ans = ''
    for j in temp:
        ans+=j+"_"
    data_all.append(ans[:len(ans)-1])

print(len(data_all))

count = 0

for i in data_all:
    if count < 17948:
        count+=1
        continue
    if count > 20000:
        print("success")
        break
    print(i+",count = "+str(count))
    try:
        firebase.put("/phishing_data",name=i,data=count)
    except Exception:
        continue
    count+=1
    
