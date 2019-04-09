from flask import Flask, render_template, request, redirect, url_for,flash
from firebase import firebase
import datetime
from firebase_admin import storage,credentials
from werkzeug import secure_filename
import firebase_admin

firebase = firebase.FirebaseApplication(
    'https://anres-test.firebaseio.com/', None)
app = Flask(__name__)


@app.route("/")
def Home():
    return render_template('home.html')


@app.route("/Search/user")
def Searchuser():
    return render_template('searchuser.html')


@app.route("/Search/suspect")
def Searchsuspect():
    return render_template('searchsuspect.html')


@app.route("/Search/case")
def Searchcase():
    return render_template('searchcase.html')


@app.route("/Search/date")
def Searchdate():
    return render_template('searchdate.html')


@app.route("/Search/type")
def Searchtype():
    return render_template('searchtype.html')


@app.route("/InfomationFromUser", methods=['POST'])
def Showuser():
    try:
        userfname = request.form['userfname']
        userlname = request.form['userlname']
        username = userfname+' '+userlname
        result = firebase.get('/users', None)
        name = []
        sussocial = []
        case = []
        susname = []
        socialtype = []
        count = []
        date = []
        key = []
        i = 0
        for Info in result:
            if (result[Info] != None):
                if (result[Info]["Name"] == username):
                    if "Name" in result[Info]:
                        name.append(result[Info]["Name"])
                    else:
                        name.append("NO Info")
                    if "Case" in result[Info]:
                        case.append(result[Info]["Case"])
                    else:
                        case.append("NO Info")
                    if "Susname" in result[Info]:
                        susname.append(result[Info]["Susname"])
                    else:
                        susname.append("NO Info")
                    if "Sussocial" in result[Info]:
                        sussocial.append(result[Info]["Sussocial"])
                    else:
                        sussocial.append("NO Info")
                    if "Type" in result[Info]:
                        socialtype.append(result[Info]["Type"])
                    else:
                        socialtype.append("NO Info")
                    sp = Info.split("-")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
        return render_template('showinfomation.html',name=name,case=case,susname=susname,sussocial=sussocial,socialtype=socialtype,date=date,count=count,key=key,show="ข้อมูลของ User")

    except:
        return render_template('no_data.html')

@app.route("/InfomationFromUser_search_fname=<fname>&&sname=<sname>", methods=['GET'])
def API_Showuser(fname,sname):
    try:
        userfname = fname
        userlname = sname
        username = userfname+' '+userlname
        result = firebase.get('/users', None)
        name = []
        sussocial = []
        case = []
        susname = []
        socialtype = []
        count = []
        date = []
        key = []
        i = 0
        for Info in result:
            if (result[Info] != None):
                if (result[Info]["Name"] == username):
                    if "Name" in result[Info]:
                        name.append(result[Info]["Name"])
                    else:
                        name.append("NO Info")
                    if "Case" in result[Info]:
                        case.append(result[Info]["Case"])
                    else:
                        case.append("NO Info")
                    if "Susname" in result[Info]:
                        susname.append(result[Info]["Susname"])
                    else:
                        susname.append("NO Info")
                    if "Sussocial" in result[Info]:
                        sussocial.append(result[Info]["Sussocial"])
                    else:
                        sussocial.append("NO Info")
                    if "Type" in result[Info]:
                        socialtype.append(result[Info]["Type"])
                    else:
                        socialtype.append("NO Info")
                    sp = Info.split("-")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
        return render_template('showinfomation.html',name=name,case=case,susname=susname,sussocial=sussocial,socialtype=socialtype,date=date,count=count,key=key,show="ข้อมูลของ User")

    except:
        return render_template('no_data.html')

@app.route("/InfomationFromSuspect", methods=['POST'])
def Showsusname():
    try:
        susfname = request.form['susfname']
        suslname = request.form['suslname']
        Susname = susfname+' '+suslname
        result = firebase.get('/users', None)
        name = []
        sussocial = []
        case = []
        susname = []
        socialtype = []
        count = []
        date = []
        key = []
        i = 0
        for Info in result:
            if (result[Info] != None):
                if (result[Info]["Susname"] == Susname):
                    if "Name" in result[Info]:
                        name.append(result[Info]["Name"])
                    else:
                        name.append("NO Info")
                    if "Case" in result[Info]:
                        case.append(result[Info]["Case"])
                    else:
                        case.append("NO Info")
                    if "Susname" in result[Info]:
                        susname.append(result[Info]["Susname"])
                    else:
                        susname.append("NO Info")
                    if "Sussocial" in result[Info]:
                        sussocial.append(result[Info]["Sussocial"])
                    else:
                        sussocial.append("NO Info")
                    if "Type" in result[Info]:
                        socialtype.append(result[Info]["Type"])
                    else:
                        socialtype.append("NO Info")
                    sp = Info.split("-")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
        return render_template('showinfomation.html',name=name,case=case,susname=susname,sussocial=sussocial,socialtype=socialtype,date=date,count=count,key=key,show="ข้อมูลของผู้ต้องสงสัย")

    except:
        return render_template('no_data.html')

@app.route("/InfomationFromSuspect_search_fname=<fname>&&sname=<sname>", methods=['GET'])
def API_Showsusname(fname,sname):
    try:
        susfname = fname
        suslname = sname
        Susname = susfname+' '+suslname
        result = firebase.get('/users', None)
        name = []
        sussocial = []
        case = []
        susname = []
        socialtype = []
        count = []
        date = []
        key = []
        i = 0
        for Info in result:
            if (result[Info] != None):
                if (result[Info]["Susname"] == Susname):
                    if "Name" in result[Info]:
                        name.append(result[Info]["Name"])
                    else:
                        name.append("NO Info")
                    if "Case" in result[Info]:
                        case.append(result[Info]["Case"])
                    else:
                        case.append("NO Info")
                    if "Susname" in result[Info]:
                        susname.append(result[Info]["Susname"])
                    else:
                        susname.append("NO Info")
                    if "Sussocial" in result[Info]:
                        sussocial.append(result[Info]["Sussocial"])
                    else:
                        sussocial.append("NO Info")
                    if "Type" in result[Info]:
                        socialtype.append(result[Info]["Type"])
                    else:
                        socialtype.append("NO Info")
                    sp = Info.split("-")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
        return render_template('showinfomation.html',name=name,case=case,susname=susname,sussocial=sussocial,socialtype=socialtype,date=date,count=count,key=key,show="ข้อมูลของผู้ต้องสงสัย")

    except:
        return render_template('no_data.html')

@app.route("/InfomationFromCase", methods=['POST'])
def Showcase():
    try:
        Case = request.form['Case']
        result = firebase.get('/users', None)
        name = []
        sussocial = []
        case = []
        susname = []
        socialtype = []
        count = []
        date = []
        key = []
        i = 0
        for Info in result:
            if (result[Info] != None):
                if (result[Info]["Case"] == Case):
                    if "Name" in result[Info]:
                        name.append(result[Info]["Name"])
                    else:
                        name.append("NO Info")
                    if "Case" in result[Info]:
                        case.append(result[Info]["Case"])
                    else:
                        case.append("NO Info")
                    if "Susname" in result[Info]:
                        susname.append(result[Info]["Susname"])
                    else:
                        susname.append("NO Info")
                    if "Sussocial" in result[Info]:
                        sussocial.append(result[Info]["Sussocial"])
                    else:
                        sussocial.append("NO Info")
                    if "Type" in result[Info]:
                        socialtype.append(result[Info]["Type"])
                    else:
                        socialtype.append("NO Info")
                    sp = Info.split("-")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
        return render_template('showinfomation.html',name=name,case=case,susname=susname,sussocial=sussocial,socialtype=socialtype,date=date,count=count,key=key,show="ข้อมูลของคดี")

    except:
        return render_template('no_data.html')

@app.route("/InfomationFromCase_search_case=<case>", methods=['GET'])
def API_Showcase(case):
    try:
        Case = case
        result = firebase.get('/users', None)
        name = []
        sussocial = []
        case = []
        susname = []
        socialtype = []
        count = []
        date = []
        key = []
        i = 0
        for Info in result:
            if (result[Info] != None):
                if (result[Info]["Case"] == Case):
                    if "Name" in result[Info]:
                        name.append(result[Info]["Name"])
                    else:
                        name.append("NO Info")
                    if "Case" in result[Info]:
                        case.append(result[Info]["Case"])
                    else:
                        case.append("NO Info")
                    if "Susname" in result[Info]:
                        susname.append(result[Info]["Susname"])
                    else:
                        susname.append("NO Info")
                    if "Sussocial" in result[Info]:
                        sussocial.append(result[Info]["Sussocial"])
                    else:
                        sussocial.append("NO Info")
                    if "Type" in result[Info]:
                        socialtype.append(result[Info]["Type"])
                    else:
                        socialtype.append("NO Info")
                    sp = Info.split("-")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
        return render_template('showinfomation.html',name=name,case=case,susname=susname,sussocial=sussocial,socialtype=socialtype,date=date,count=count,key=key,show="ข้อมูลของคดี")

    except:
        return render_template('no_data.html')

@app.route("/InfomationFromDate", methods=['POST'])
def Showdate():
    Date = request.form['Date']
    try:
        result = firebase.get('/users', None)
        name = []
        sussocial = []
        case = []
        susname = []
        socialtype = []
        count = []
        date = []
        key = []
        i = 0
        for Info in result:
            sp = Info.split("-")
            dsp = Date.split("-")
            if ((dsp[0] == sp[2]) and (dsp[1] == sp[1]) and (dsp[2] == sp[0])):
                if (result[Info] != None):
                    if "Name" in result[Info]:
                        name.append(result[Info]["Name"])
                    else:
                        name.append("NO Info")
                    if "Case" in result[Info]:
                        case.append(result[Info]["Case"])
                    else:
                        case.append("NO Info")
                    if "Susname" in result[Info]:
                        susname.append(result[Info]["Susname"])
                    else:
                        susname.append("NO Info")
                    if "Sussocial" in result[Info]:
                        sussocial.append(result[Info]["Sussocial"])
                    else:
                        sussocial.append("NO Info")
                    if "Type" in result[Info]:
                        socialtype.append(result[Info]["Type"])
                    else:
                        socialtype.append("NO Info")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
                    return render_template('showinfomation.html',name=name,case=case,susname=susname,sussocial=sussocial,socialtype=socialtype,date=date,count=count,key=key,show="ข้อมูลของวันที่แจ้งเหตุ")

    except :
        return "Don't Have any Day that you want"        
    
@app.route("/InfomationFromDate_search_date=<date>", methods=['GET'])
def API_Showdate(date):
    Date = date
    try:
        result = firebase.get('/users', None)
        name = []
        sussocial = []
        case = []
        susname = []
        socialtype = []
        count = []
        date = []
        key = []
        i = 0
        for Info in result:
            sp = Info.split("-")
            dsp = Date.split("_")
            if ((dsp[0] == sp[2]) and (dsp[1] == sp[1]) and (dsp[2] == sp[0])):
                if (result[Info] != None):
                    if "Name" in result[Info]:
                        name.append(result[Info]["Name"])
                    else:
                        name.append("NO Info")
                    if "Case" in result[Info]:
                        case.append(result[Info]["Case"])
                    else:
                        case.append("NO Info")
                    if "Susname" in result[Info]:
                        susname.append(result[Info]["Susname"])
                    else:
                        susname.append("NO Info")
                    if "Sussocial" in result[Info]:
                        sussocial.append(result[Info]["Sussocial"])
                    else:
                        sussocial.append("NO Info")
                    if "Type" in result[Info]:
                        socialtype.append(result[Info]["Type"])
                    else:
                        socialtype.append("NO Info")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
                    return render_template('showinfomation.html',name=name,case=case,susname=susname,sussocial=sussocial,socialtype=socialtype,date=date,count=count,key=key,show="ข้อมูลของวันที่แจ้งเหตุ")

    except :
        # flash("Don't Have any Day that you want")
        return render_template('no_data.html') 

@app.route("/InfomationFromType", methods=['POST'])
def Showtype():
    try:
        Type = request.form['Type']
        result = firebase.get('/users', None)
        name = []
        sussocial = []
        case = []
        susname = []
        socialtype = []
        count = []
        date = []
        key = []
        i = 0
        for Info in result:
            if (result[Info] != None):
                if (result[Info]["Type"] == Type):
                    if "Name" in result[Info]:
                        name.append(result[Info]["Name"])
                    else:
                        name.append("NO Info")
                    if "Case" in result[Info]:
                        case.append(result[Info]["Case"])
                    else:
                        case.append("NO Info")
                    if "Susname" in result[Info]:
                        susname.append(result[Info]["Susname"])
                    else:
                        susname.append("NO Info")
                    if "Sussocial" in result[Info]:
                        sussocial.append(result[Info]["Sussocial"])
                    else:
                        sussocial.append("NO Info")
                    if "Type" in result[Info]:
                        socialtype.append(result[Info]["Type"])
                    else:
                        socialtype.append("NO Info")
                    sp = Info.split("-")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
        return render_template('showinfomation.html',name=name,case=case,susname=susname,sussocial=sussocial,socialtype=socialtype,date=date,count=count,key=key,show="ข้อมูลของประเภท")
    except:
        return render_template('no_data.html')

@app.route("/InfomationFromType_search_type=<typee>", methods=['GET'])
def API_Showtype(typee):
    try:
        Type = typee
        result = firebase.get('/users', None)
        name = []
        sussocial = []
        case = []
        susname = []
        socialtype = []
        count = []
        date = []
        key = []
        i = 0
        for Info in result:
            if (result[Info] != None):
                if (result[Info]["Type"] == Type):
                    if "Name" in result[Info]:
                        name.append(result[Info]["Name"])
                    else:
                        name.append("NO Info")
                    if "Case" in result[Info]:
                        case.append(result[Info]["Case"])
                    else:
                        case.append("NO Info")
                    if "Susname" in result[Info]:
                        susname.append(result[Info]["Susname"])
                    else:
                        susname.append("NO Info")
                    if "Sussocial" in result[Info]:
                        sussocial.append(result[Info]["Sussocial"])
                    else:
                        sussocial.append("NO Info")
                    if "Type" in result[Info]:
                        socialtype.append(result[Info]["Type"])
                    else:
                        socialtype.append("NO Info")
                    sp = Info.split("-")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
        return render_template('showinfomation.html',name=name,case=case,susname=susname,sussocial=sussocial,socialtype=socialtype,date=date,count=count,key=key,show="ข้อมูลของประเภท")
    except:
        return render_template('no_data.html')


@app.route("/ShowAll")
def showData():
    result = firebase.get('/users', None)
    name = []
    sussocial = []
    case = []
    susname = []
    socialtype = []
    count = []
    date = []
    key = []
    i = 0
    for Info in result:
        if result[Info] != None:
            if "Name" in result[Info]:
                name.append(result[Info]["Name"])
            else:
                name.append("NO Info")
            if "Case" in result[Info]:
                case.append(result[Info]["Case"])
            else:
                case.append("NO Info")
            if "Susname" in result[Info]:
                susname.append(result[Info]["Susname"])
            else:
                susname.append("NO Info")
            if "Sussocial" in result[Info]:
                sussocial.append(result[Info]["Sussocial"])
            else:
                sussocial.append("NO Info")
            if "Type" in result[Info]:
                socialtype.append(result[Info]["Type"])
            else:
                socialtype.append("NO Info")
            sp = Info.split("-")
            d = sp[2]+'/'+sp[1]+'/20'+sp[0]
            date.append(d)
            key.append(Info)
            count.append(i)
            i += 1
    return render_template('index.html',name=name,case=case,susname=susname,sussocial=sussocial,socialtype=socialtype,date=date,count=count,key=key)


@app.route("/InsertData")
def showForm():
    return render_template('adddata.html')


@app.route("/insert", methods=['POST'])
def insert():
    if request.method == 'POST':
        userfname = request.form['userfname']
        userlname = request.form['userlname']
        useremail = request.form['useremail']
        usertel = request.form['usertel']
        CaseType = request.form['Type']
        Sussocial = request.form['Sussocial']
        Susfname = request.form['Susfname']
        Suslname = request.form['Suslname']
        username = userfname+' '+userlname
        if ((Susfname != '-') and (Suslname)):
            Susname = Susfname+' '+Suslname
        else:
            Susname = '-'
        Case = request.form['Case']
        time = datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")
        pth = '/users/'+time
        firebase.put(pth, name="Name", data=username)
        firebase.put(pth, name="E-mail", data=useremail)
        firebase.put(pth, name="Tel", data=usertel)
        firebase.put(pth, name="Type", data=CaseType)
        firebase.put(pth, name="Sussocial", data=Sussocial)
        firebase.put(pth, name="Susname", data=Susname)
        firebase.put(pth, name="Case", data=Case)
        name_sum = userfname+'_'+userlname
        img = request.files['image']
        filename = secure_filename(img.filename)
        img.save('upload/'+name_sum+"_"+time+filename)
        cred = credentials.Certificate('anres-test-firebase-adminsdk-4z967-07c79cd90f.json')
        firebase_admin.initialize_app(cred, {'storageBucket': 'anres-test.appspot.com'})
        bucket = storage.bucket()
        blob = bucket.blob(name_sum+'/'+time+"T"+filename)
        blob.upload_from_filename('upload/'+name_sum+"_"+time+filename)
        firebase.put(pth, name="Image", data=time+"T"+filename)
        return render_template('Thanks.html')


@app.route("/delete/<string:key_data>", methods=['GET'])
def delete(key_data):
    firebase.delete('/users', key_data)
    return redirect(url_for('showData'))


@app.route("/update", methods=['POST'])
def update():
    if request.method == 'POST':
        updatekey = request.form['id']
        username = request.form['username']
        userage = request.form['userage']
        usertel = request.form['usertel']
        pth = '/users/'+(updatekey)
        firebase.put(pth, name="Name", data=username)
        firebase.put(pth, name="Age", data=userage)
        firebase.put(pth, name="Tel", data=usertel)
        return redirect(url_for('showData'))


if __name__ == "__main__":
    app.run(debug=True)
