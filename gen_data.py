from firebase import firebase
import random
import pandas
import string

firebase = firebase.FirebaseApplication('https://test-database-anres.firebaseio.com', None)

def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

def gen_date():
    d = str(random.randint(1,31))
    if len(d) == 1:
        d = '0'+d
    h = str(random.randint(0,24))
    if len(h) == 1:
        h = '0'+h
    m = str(random.randint(0,60))
    if len(m) == 1:
        m = '0'+m
    s = str(random.randint(0,60))
    if len(s) == 1:
        s = '0'+s

    time = '19-04-'+d+'-'+h+'-'+m+'-'+s
    return time

# time = datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")

df = pandas.read_csv('DatabaseNISIT.csv')

df_fname = list(df["STD_FIRST_NAME"])
df_lname = list(df["STD_LAST_NAME"])
df_email = list(df["e-mail"])

case = ["Hacking_to_modify_or_steal_or_destroy_Data","Selling_products_or_Services_scam","Fake_to_others","Scam_to_transfer_money","Email_scam","Romance_scam","Blackmail","Defamation"]

case_type = ["Facebook","E-mail","Website","Line"]

name = []

for i in range(len(df_fname)):
    l = random.randint(0,len(df_lname)-1)
    if(l == i):
        l+=1
    name.append(df_fname[i]+' '+df_lname[l])

# Sussocial = df_email[0].split('@')[0]
# print(Sussocial)


# print(df_fname)
# print('.......')
# print(df_lname)

# print(name)
#print(len(df_email))

# random.randint()

for i in range(10):
    time = gen_date()
    pth = '/users/'+time
    uname = random.randint(0,len(name)-1)
    utel = random.randint(0,999999999)
    uage = random.randint(19,24)
    c = random.randint(0,len(case)-1)
    sname = random.randint(0,len(name)-1)
    Other = random_char(random.randint(10,24))
    if sname == uname:
        sname+=1
    t = random.randint(0,len(case_type)-1)
    m = random.randint(0,4)

    username = name[uname]
    firebase.put(pth, name="Name", data=username)

    useremail = df_email[uname]
    firebase.put(pth, name="E-mail", data=useremail)

    usertel = str(utel)
    while len(usertel) < 10:
        usertel = "0"+usertel
    firebase.put(pth, name="Tel", data=usertel)

    userage = uage
    firebase.put(pth, name="Age", data=userage)

    if case[c] == "Email_scam":
        CaseType = "E-mail"
    else:
        CaseType = case_type[t]
    firebase.put(pth, name="Type", data=CaseType)

    if CaseType == "Line":
        Sussocial = df_email[sname].split('@')[0]
    elif CaseType == "Facebook":
         Sussocial = ((df_email[sname].split('@')[0]).split('.')[0])+' '+((df_email[sname].split('@')[0]).split('.')[1])
    elif CaseType == "E-mail":
        Sussocial = df_email[sname]
    else:
        Sussocial = 'http://www.'+((df_email[sname].split('@')[0]).split('.')[0])+'.com'

    firebase.put(pth, name="Sussocial", data=Sussocial)

    Susname = name[sname]
    firebase.put(pth, name="Susname", data=Susname)

    Case = case[c]
    firebase.put(pth, name="Case", data=Case)

    firebase.put(pth, name="Other", data=Other)

    if(m == 0):
        firebase.put(pth, name="Gender", data="M")
    
    elif (m == 1):
        firebase.put(pth, name="Gender", data="A")
    
    else:
        firebase.put(pth, name="Gender", data="F")


    

    print(i,'=',username,useremail,usertel,userage,CaseType,Sussocial,Susname,Case,Other)

print("Finish")