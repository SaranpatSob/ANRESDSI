import json

def return_json(name,case,susname,sussocial,typee):
    ans = []
    for i in range(max(len(name),len(case),len(susname),len(sussocial),len(typee))):
        ans.append({})
        ans[i].setdefault("Name",name[i])
        ans[i].setdefault("Case",case[i])
        ans[i].setdefault("SusName",susname[i])
        ans[i].setdefault("SusSocial",sussocial[i])
        ans[i].setdefault("Type",typee[i])
    #print(ans)
    # a = json.dumps(ans,ensure_ascii=False)
    return json.dumps(ans,ensure_ascii=False)
    

# import pandas as pd 

# df = pd.DataFrame([['a', 'b'], ['c', 'd']],index=['row 1', 'row 2'],columns=['col 1', 'col 2'])

# df.to_json(orient='split')

# print(df)

if __name__ == "__main__":
    Date = ['ก',3,4,12,7,5,3,11,1,4,6,7,9,10]
    print(return_json(Date,Date,Date,Date,Date))