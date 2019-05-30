from flask import Flask, render_template, request, redirect, url_for, flash,jsonify,make_response,session
from firebase import firebase
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import datetime
from firebase_admin import storage, credentials
from werkzeug import secure_filename
import firebase_admin
from return_json import return_json
import os

firebase = firebase.FirebaseApplication(
    'https://test-database-anres.firebaseio.com', None)
app = Flask(__name__)

app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app) 

def set_susname(susname):
    for i in range(len(susname)):
            if len(susname[i].split('_')) > 1:
                susname[i] = susname[i].split('_')[0] + ' '  + susname[i].split('_')[1]
    return susname

@app.route("/")
def Home():
    return render_template('home1.html')


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


@app.route("/InformationFromUser", methods=['POST'])
def Showuser():
    try:
        userfname = request.form['userfname']
        userlname = request.form['userlname']
        username = userfname+'_'+userlname
        result = firebase.get('/users', None)
        name = []
        sussocial = []
        case = []
        susname = []
        socialtype = []
        count = []
        date = []
        key = []
        gender = []
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
                        temp = result[Info]["Susname"].split('_')
                        nt = temp[0]+" "+temp[1]
                        susname.append(nt)
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
                    if "Gender" in result[Info]:
                        if(result[Info]["Gender"] == "M"):
                            gender.append("Male")
                        elif (result[Info]["Gender"] == "F"):
                            gender.append("Female")
                        else:
                            gender.append("Alternative sex")
                        # gender.append(result[Info]["Gender"])
                    else:
                        gender.append("NO Info")
                    sp = Info.split("-")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
        return render_template('showinformation.html', name=name, case=case, susname=susname, sussocial=sussocial, socialtype=socialtype, date=date, count=count, key=key, show="ข้อมูลของ User", gender=gender)

    except:
        return render_template('no_data.html')


@app.route("/InformationFromUser_search_fname=<fname>&&sname=<sname>", methods=['GET'])
def API_Showuser(fname, sname):
    try:
        userfname = fname.lower()
        userlname = sname.lower()
        username = userfname+'_'+userlname
        result = firebase.get('/users', None)
        name = []
        sussocial = []
        case = []
        susname = []
        socialtype = []
        count = []
        date = []
        key = []
        gender = []
        i = 0
        for Info in result:
            if (result[Info] != None):
                if (result[Info]["Name"].lower() == username):
                    if "Name" in result[Info]:
                        temp = result[Info]["Name"].split('_')
                        nt = temp[0]+' '+temp[1]
                        name.append(nt)
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
                    if "Gender" in result[Info]:
                        if(result[Info]["Gender"] == "M"):
                            gender.append("Male")
                        elif (result[Info]["Gender"] == "F"):
                            gender.append("Female")
                        else:
                            gender.append("Alternative sex")
                        # gender.append(result[Info]["Gender"])
                    else:
                        gender.append("NO Info")
                    sp = Info.split("-")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
        resp = make_response(return_json(name, case, susname, sussocial, socialtype, gender))
        resp.headers['Content-Type'] = 'application/json'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except:
        return render_template('no_data.html')


@app.route("/InformationFromSuspect", methods=['POST'])
def Showsusname():
    try:
        susfname = request.form['susfname']
        suslname = request.form['suslname']
        Susname = susfname+' '+suslname
        Susname1 = susfname+'_'+suslname
        result = firebase.get('/users', None)
        name = []
        sussocial = []
        case = []
        susname = []
        socialtype = []
        count = []
        date = []
        key = []
        gender = []
        i = 0
        for Info in result:
            if (result[Info] != None):
                if (result[Info]["Susname"].lower() == Susname.lower() or result[Info]["Susname"].lower() == Susname1.lower()):
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
                    if "Gender" in result[Info]:
                        if(result[Info]["Gender"] == "M"):
                            gender.append("Male")
                        elif (result[Info]["Gender"] == "F"):
                            gender.append("Female")
                        else:
                            gender.append("Alternative sex")
                        # gender.append(result[Info]["Gender"])
                    else:
                        gender.append("NO Info")
                    sp = Info.split("-")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
        susname = set_susname(susname)
        return render_template('showinformation.html', name=name, case=case, susname=susname, sussocial=sussocial, socialtype=socialtype, date=date, count=count, key=key, gender = gender, show="ข้อมูลของผู้ต้องสงสัย")

    except:
        return render_template('no_data.html')


@app.route("/InformationFromSuspect_search_fname=<fname>&&sname=<sname>", methods=['GET'])
def API_Showsusname(fname, sname):
    try:
        susfname = fname
        suslname = sname
        Susname = susfname+' '+suslname
        Susname1 = susfname+'_'+suslname
        result = firebase.get('/users', None)
        name = []
        sussocial = []
        case = []
        susname = []
        socialtype = []
        count = []
        date = []
        key = []
        gender = []
        i = 0
        for Info in result:
            if (result[Info] != None):
                if (result[Info]["Susname"].lower() == Susname.lower() or result[Info]["Susname"].lower() == Susname1.lower()):
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
                    if "Gender" in result[Info]:
                        if(result[Info]["Gender"] == "M"):
                            gender.append("Male")
                        elif (result[Info]["Gender"] == "F"):
                            gender.append("Female")
                        else:
                            gender.append("Alternative sex")
                        # gender.append(result[Info]["Gender"])
                    else:
                        gender.append("NO Info")
                    sp = Info.split("-")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
        susname = set_susname(susname)
        resp = make_response(return_json(name, case, susname, sussocial, socialtype, gender))
        resp.headers['Content-Type'] = 'application/json'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except:
        return render_template('no_data.html')


@app.route("/InformationFromCase", methods=['POST'])
def Showcase():
    #try:
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
        gender = []
        i = 0
        for Info in result:
            if (result[Info] != None):
                if (result[Info]["Case"] == Case):
                    if "Name" in result[Info]:
                        name.append(result[Info]["Name"])
                    else:
                        name.append("NO Info")
                    if "Case" in result[Info]:
                        # temp = result[Info]["Case"]
                        # temp = temp.split('_')
                        # anss = ''
                        # for i in range(len(temp)):
                        #     anss = anss+temp[i]+" "
                        # case.append(anss[0:len(anss)])
                        # return str(type(result[Info]["Case"])).split("'")[1]
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
                    if "Gender" in result[Info]:
                        if(result[Info]["Gender"] == "M"):
                            gender.append("Male")
                        elif (result[Info]["Gender"] == "F"):
                            gender.append("Female")
                        else:
                            gender.append("Alternative sex")
                        # gender.append(result[Info]["Gender"])
                    else:
                        gender.append("NO Info")
                    sp = Info.split("-")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
        susname = set_susname(susname)
        # return str(name)
        return render_template('showinformation.html', name=name, case=case, susname=susname, sussocial=sussocial, socialtype=socialtype, date=date, count=count, key=key, gender = gender, show="ข้อมูลของคดี")

    #except:
        #return render_template('no_data.html')


@app.route("/InformationFromCase_search_case=<case>", methods=['GET'])
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
        gender = []
        i = 0
        for Info in result:
            if (result[Info] != None):
                if ((result[Info]['Case']).lower() == Case.lower()):
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
                    if "Gender" in result[Info]:
                        if(result[Info]["Gender"] == "M"):
                            gender.append("Male")
                        elif (result[Info]["Gender"] == "F"):
                            gender.append("Female")
                        else:
                            gender.append("Alternative sex")
                        # gender.append(result[Info]["Gender"])
                    else:
                        gender.append("NO Info")
                    sp = Info.split("-")
                    
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1

        susname = set_susname(susname)
        resp = make_response(return_json(name, case, susname, sussocial, socialtype, gender))
        resp.headers['Content-Type'] = 'application/json'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except :
        return render_template('no_data.html')
   


@app.route("/InformationFromDate", methods=['POST'])
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
        gender = []
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
                    if "Gender" in result[Info]:
                        if(result[Info]["Gender"] == "M"):
                            gender.append("Male")
                        elif (result[Info]["Gender"] == "F"):
                            gender.append("Female")
                        else:
                            gender.append("Alternative sex")
                        # gender.append(result[Info]["Gender"])
                    else:
                        gender.append("NO Info")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
        susname = set_susname(susname)
        return render_template('showinformation.html', name=name, case=case, susname=susname, sussocial=sussocial, socialtype=socialtype, date=date, count=count, key=key, gender=gender, show="ข้อมูลของวันที่แจ้งเหตุ")
    except:
        # flash("Don't Have any Day that you want")
        return render_template('no_data.html')

    # try:
    #     result = firebase.get('/users', None)
    #     name = []
    #     sussocial = []
    #     case = []
    #     susname = []
    #     socialtype = []
    #     count = []
    #     date = []
    #     key = []
    #     i = 0
    #     for Info in result:
    #         sp = Info.split("-")
    #         dsp = Date.split("-")
    #         if ((dsp[0] == sp[2]) and (dsp[1] == sp[1]) and (dsp[2] == sp[0])):
    #             if (result[Info] != None):
    #                 if "Name" in result[Info]:
    #                     name.append(result[Info]["Name"])
    #                 else:
    #                     name.append("NO Info")
    #                 if "Case" in result[Info]:
    #                     case.append(result[Info]["Case"])
    #                 else:
    #                     case.append("NO Info")
    #                 if "Susname" in result[Info]:
    #                     temp = result[Info]["Susname"].split('_')
    #                     nt = temp[0]+" "+temp[1]
    #                     susname.append(nt)
    #                 else:
    #                     susname.append("NO Info")
    #                 if "Sussocial" in result[Info]:
    #                     sussocial.append(result[Info]["Sussocial"])
    #                 else:
    #                     sussocial.append("NO Info")
    #                 if "Type" in result[Info]:
    #                     socialtype.append(result[Info]["Type"])
    #                 else:
    #                     socialtype.append("NO Info")
    #                 d = sp[2]+'/'+sp[1]+'/20'+sp[0]
    #                 date.append(d)
    #                 key.append(Info)
    #                 count.append(i)
    #                 i += 1
    #                 return render_template('showinformation.html', name=name, case=case, susname=susname, sussocial=sussocial, socialtype=socialtype, date=date, count=count, key=key, show="ข้อมูลของวันที่แจ้งเหตุ")

    # except:
    #     return render_template("no_data.html")


@app.route("/InformationFromDate_search_date=<date>", methods=['GET'])
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
        gender = []
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
                    if "Gender" in result[Info]:
                        if(result[Info]["Gender"] == "M"):
                            gender.append("Male")
                        elif (result[Info]["Gender"] == "F"):
                            gender.append("Female")
                        else:
                            gender.append("Alternative sex")
                        # gender.append(result[Info]["Gender"])
                    else:
                        gender.append("NO Info")
                    d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                    date.append(d)
                    key.append(Info)
                    count.append(i)
                    i += 1
        susname = set_susname(susname)
        resp = make_response(return_json(name, case, susname, sussocial, socialtype, gender))
        resp.headers['Content-Type'] = 'application/json'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except:
        # flash("Don't Have any Day that you want")
        return render_template('no_data.html')


@app.route("/InformationFromType", methods=['POST'])
def Showtype():
    #try:
        result = firebase.get('/users', None)
        Type = request.form['Type']
        if (Type == "Facebook"):
            Sussocial = request.form['Susfacebook']
        elif (Type == "E-mail"):
            Sussocial = request.form['Susemail']
        elif (Type == "Website"):
            Sussocial = request.form['Susurl']
        else:
            Sussocial = request.form['Susline']
        name = []
        sussocial = []
        case = []
        susname = []
        socialtype = []
        count = []
        date = []
        key = []
        gender = []
        i = 0
        for Info in result:
            if (result[Info] != None):
                if (result[Info]["Type"] == Type):
                    if (result[Info]["Sussocial"] == Sussocial):
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
                        if "Gender" in result[Info]:
                            if(result[Info]["Gender"] == "M"):
                                gender.append("Male")
                            elif (result[Info]["Gender"] == "F"):
                                gender.append("Female")
                            else:
                                gender.append("Alternative sex")
                            # gender.append(result[Info]["Gender"])
                        else:
                            gender.append("NO Info")
                        sp = Info.split("-")
                        d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                        date.append(d)
                        key.append(Info)
                        count.append(i)
                        i += 1
        susname = set_susname(susname)
        return render_template('showinformation.html', name=name, case=case, susname=susname, sussocial=sussocial, socialtype=socialtype, date=date, count=count, key=key, gender = gender, show="ข้อมูลของประเภท")
    # except:
    #     return render_template('no_data.html')


@app.route("/InformationFromType_search_type=<typee>&&sussocial=<sussocialinp>", methods=['GET'])
def API_Showtype(typee,sussocialinp):
    try:
        result = firebase.get('/users', None)
        Type = typee
        # if (Type == "Facebook"):
        #     Sussocial = request.form['Susfacebook']
        # elif (Type == "E-mail"):
        #     Sussocial = request.form['Susemail']
        # elif (Type == "Website"):
        #     Sussocial = request.form['Susurl']
        # else:
        #     Sussocial = request.form['Susline']
        Sussocial = sussocialinp
        name = []
        sussocial = []
        case = []
        susname = []
        socialtype = []
        count = []
        date = []
        key = []
        gender = []
        i = 0
        for Info in result:
            if (result[Info] != None):
                if (result[Info]["Type"].lower() == Type.lower()):
                    if (result[Info]["Sussocial"] == Sussocial):
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
                        if "Gender" in result[Info]:
                            if(result[Info]["Gender"] == "M"):
                                gender.append("Male")
                            elif (result[Info]["Gender"] == "F"):
                                gender.append("Female")
                            else:
                                gender.append("Alternative sex")
                            # gender.append(result[Info]["Gender"])
                        else:
                            gender.append("NO Info")
                        sp = Info.split("-")
                        d = sp[2]+'/'+sp[1]+'/20'+sp[0]
                        date.append(d)
                        key.append(Info)
                        count.append(i)
                        i += 1
        susname = set_susname(susname)
        resp = make_response(return_json(name, case, susname, sussocial, socialtype,gender))
        resp.headers['Content-Type'] = 'application/json'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except:
        return render_template('no_data.html')



@app.route("/ShowAll")
def showData():
    result = firebase.get('/users', None)
    name = []
    sussocial = []
    age = []
    case = []
    susname = []
    socialtype = []
    count = []
    date = []
    other = []
    email = []
    tel = []
    key = []
    gender = []
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
                # temp = result[Info]["Susname"].split('_')
                # nt = temp[0]+" "+temp[1]
                # susname.append(nt)
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
            if "Age" in result[Info]:
                age.append(result[Info]["Age"])
            else:
                age.append("NO Info")
            if "Other" in result[Info]:
                other.append(result[Info]["Other"])
            else:
                other.append("NO Info")
            if "E-mail" in result[Info]:
                email.append(result[Info]["E-mail"])
            else:
                email.append("NO Info")
            if "Tel" in result[Info]:
                tel.append(result[Info]["Tel"])
            else:
                tel.append("NO Info")
            if "Gender" in result[Info]:
                if(result[Info]["Gender"] == "M"):
                    gender.append("Male")
                elif (result[Info]["Gender"] == "F"):
                    gender.append("Female")
                else:
                    gender.append("Alternative sex")
                # # gender.append(result[Info]["Gender"])
            else:
                gender.append("NO Info")
            sp = Info.split("-")
            d = sp[2]+'/'+sp[1]+'/20'+sp[0]
            date.append(d)
            key.append(Info)
            count.append(i)
            i += 1
    susname = set_susname(susname)
    return render_template('index.html', name=name, case=case, susname=susname, sussocial=sussocial, socialtype=socialtype, date=date, count=count, key=key, age=age, other=other, email=email, tel=tel, gender = gender)

@app.route("/ShowAll_API",methods = ['GET'])
def APIshowData():
    result = firebase.get('/users', None)
    name = []
    sussocial = []
    age = []
    case = []
    susname = []
    socialtype = []
    count = []
    date = []
    other = []
    email = []
    tel = []
    key = []
    gender = []
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
                # temp = result[Info]["Susname"].split('_')
                # nt = temp[0]+" "+temp[1]
                # susname.append(nt)
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
            if "Age" in result[Info]:
                age.append(result[Info]["Age"])
            else:
                age.append("NO Info")
            if "Other" in result[Info]:
                other.append(result[Info]["Other"])
            else:
                other.append("NO Info")
            if "E-mail" in result[Info]:
                email.append(result[Info]["E-mail"])
            else:
                email.append("NO Info")
            if "Tel" in result[Info]:
                tel.append(result[Info]["Tel"])
            else:
                tel.append("NO Info")
            if "Gender" in result[Info]:
                if(result[Info]["Gender"] == "M"):
                    gender.append("Male")
                elif (result[Info]["Gender"] == "F"):
                    gender.append("Female")
                else:
                    gender.append("Alternative sex")
                # # gender.append(result[Info]["Gender"])
            else:
                gender.append("NO Info")
            sp = Info.split("-")
            d = sp[2]+'/'+sp[1]+'/20'+sp[0]
            date.append(d)
            key.append(Info)
            count.append(i)
            i += 1
    resp = make_response(return_json(name, case, susname, sussocial, socialtype, gender))
    resp.headers['Content-Type'] = 'application/json'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
    # return result


@app.route("/InsertData")
def showForm():
    return render_template('adddata.html')


@app.route("/insert", methods=['POST'])
def insert():
    if request.method == 'POST':
        userfname = request.form['userfname']
        userlname = request.form['userlname']
        useremail = request.form['useremail']
        userage = request.form['userage']
        usertel = request.form['usertel']
        CaseType = request.form['Type']
        Case = request.form['Case']
        Susfname = request.form['Susfname']
        Suslname = request.form['Suslname']
        Other = request.form['Other']
        username = userfname+'_'+userlname
        if (CaseType == "Facebook"):
            Sussocial = request.form['Susfacebook']
        elif (CaseType == "E-mail"):
            Sussocial = request.form['Susemail']
        elif (CaseType == "Website"):
            Sussocial = request.form['Susurl']
        else:
            Sussocial = request.form['Susline']
        if ((Susfname != '-') and (Suslname != '-')):
            Susname = Susfname+' '+Suslname
        else:
            Susname = '-'
        time = datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")
        pth = '/users/'+time
        firebase.put(pth, name="Name", data=username)
        firebase.put(pth, name="E-mail", data=useremail)
        firebase.put(pth, name="Tel", data=usertel)
        firebase.put(pth, name="Age", data=userage)
        firebase.put(pth, name="Type", data=CaseType)
        firebase.put(pth, name="Sussocial", data=Sussocial)
        firebase.put(pth, name="Susname", data=Susname)
        firebase.put(pth, name="Case", data=Case)
        firebase.put(pth, name="Other", data=Other)
        name_sum = userfname+'_'+userlname
        # img = request.files['image']
        img = request.files("image")
        k = 1
        for i in img:
            fille = request.files.get(i)
            filename = photos.save(fille,name=fille.filename)
            # filename = secure_filename(i.filename)
            # i.save('upload/'+name_sum+"_"+time+filename)
            cred = credentials.Certificate(
                'anres-test-firebase-adminsdk-4z967-07c79cd90f.json')
            firebase_admin.initialize_app(
                cred, {'storageBucket': 'anres-test.appspot.com'})
            bucket = storage.bucket()
            blob = bucket.blob(name_sum+'/'+time+"T"+filename)
            blob.upload_from_filename('upload/'+name_sum+"_"+time+filename)
            firebase.put(pth, name="Image"+str(k), data=time+"T"+filename)
            k += 1
        return render_template('Thanks.html')


@app.route("/delete/<string:key_data>", methods=['GET'])
def delete(key_data):
    firebase.delete('/users', key_data)
    return redirect(url_for('showData'))


@app.route("/update", methods=['POST'])
def update():
    if request.method == 'POST':
        updatekey = request.form['id']
        userfname = request.form['userfname']
        userlname = request.form['userlname']
        userage = request.form['userage']
        useremail = request.form['useremail']
        usertel = request.form['usertel']
        CaseType = request.form['Type']
        Case = request.form['Case']
        Sussocial = request.form['Sussocial']
        Susfname = request.form['Susfname']
        Suslname = request.form['Suslname']
        Other = request.form['Other']
        username = userfname+'_'+userlname
        if ((Susfname != '-') and (Suslname)):
            Susname = Susfname+'_'+Suslname
        else:
            Susname = '-'
        pth = '/users/'+(updatekey)
        firebase.put(pth, name="Name", data=username)
        firebase.put(pth, name="E-mail", data=useremail)
        firebase.put(pth, name="Tel", data=usertel)
        firebase.put(pth, name="Age", data=userage)
        firebase.put(pth, name="Type", data=CaseType)
        firebase.put(pth, name="Sussocial", data=Sussocial)
        firebase.put(pth, name="Susname", data=Susname)
        firebase.put(pth, name="Case", data=Case)
        firebase.put(pth, name="Other", data=Other)
        return redirect(url_for('showData'))


if __name__ == "__main__":
    app.run(debug=True)
