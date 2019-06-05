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
i = 0

while i < (len(data_all)):
    # print(i+",count = "+str(count))
    try:
        result = firebase.get("/phishing_data",data_all[i])
        print(result)
        if result is None:
            print("Add  "+i+",count = "+str(count))
            firebase.put("/phishing_data",name=data_all[i],data=count)
        count+=1
        i+=1
    except Exception:
        continue
    
