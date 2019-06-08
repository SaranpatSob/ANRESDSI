import pandas as pd 
import numpy as np 
from firebase import firebase

firebase = firebase.FirebaseApplication('https://test-database-anres.firebaseio.com', None)

dt = np.array(pd.read_csv("domain.txt"))

data_all = []

inp = int(input())
inp = inp*10000

for i in dt:
    temp = i[0].split('.')
    ans = ''
    for j in temp:
        ans+=j+"_"
    data_all.append(ans[:len(ans)-1])

print(len(data_all))

count = 0

i=0

while i < len(data_all):
# for i in range(len(data_all)):
    if count < inp:
        count+=1
        i+=1
        continue
    if count > inp+10000:
        print("success")
        break
    print(data_all[i]+",count = "+str(count))
    try:
        firebase.put("/phishing_data",name=data_all[i],data=count)
        i+=1
    except Exception:
        i-=1
        continue
    count+=1
    
