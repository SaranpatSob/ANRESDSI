from flask import Flask, render_template, request, redirect, url_for
from firebase import firebase
import datetime

firebase = firebase.FirebaseApplication(
    'https://test-database-anres.firebaseio.com', None)
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
    return render_template('showinfomation.html',name=name,case=case,susname=susname,sussocial=sussocial,socialtype=socialtype,date=date,count=count,key=key)


@app.route("/InfomationFromSuspect", methods=['POST'])
def Showsusname():
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
    return render_template('showinfomation.html',name=name,case=case,susname=susname,sussocial=sussocial,socialtype=socialtype,date=date,count=count,key=key)


@app.route("/InfomationFromCase", methods=['POST'])
def Showcase():
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
    return render_template('showinfomation.html',name=name,case=case,susname=susname,sussocial=sussocial,socialtype=socialtype,date=date,count=count,key=key)


@app.route("/InfomationFromDate", methods=['POST'])
def Showdate():
    Date = request.form['Date']
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
        dsp = Date.split("/")
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
    return render_template('showinfomation.html',name=name,case=case,susname=susname,sussocial=sussocial,socialtype=socialtype,date=date,count=count,key=key)


@app.route("/InfomationFromType", methods=['POST'])
def Showtype():
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
    return render_template('showinfomation.html',name=name,case=case,susname=susname,sussocial=sussocial,socialtype=socialtype,date=date,count=count,key=key)


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
        pth = '/users/'+(datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
        firebase.put(pth, name="Name", data=username)
        firebase.put(pth, name="E-mail", data=useremail)
        firebase.put(pth, name="Tel", data=usertel)
        firebase.put(pth, name="Type", data=CaseType)
        firebase.put(pth, name="Sussocial", data=Sussocial)
        firebase.put(pth, name="Susname", data=Susname)
        firebase.put(pth, name="Case", data=Case)
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
