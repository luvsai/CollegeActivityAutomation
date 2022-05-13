from cgitb import html
import imp
import re
from tkinter import E
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .forms import *
from .models import  *
import json
from django.views.decorators.csrf import csrf_exempt
import random
import string
from .signutilities import *
from .forms import faculty_publications, Profile_Form
from . import datauti
from django.shortcuts import redirect
from IPython.display import HTML
import pandas as pd

user=''
pwd=''


facpubdict = datauti.get_publications_Faculty("")
dodata = [
  
  ['pub', 'Count']
  
]


def gettfcount(fid) : 
    print(facpubdict)
    tpcount = 0
    for k, v in facpubdict.items():
        tpcount = tpcount+len(v)
    fcount = len(facpubdict[fid])
    tpcount -= fcount
    return [tpcount,fcount]
def getdodata(lis):
    ddod = dodata[:]
    ddod.append(['Others',     lis[0]])
    ddod.append(['Your Contribution',     lis[1]])
    return ddod

@csrf_exempt
def crlogin(request):
    global user,pwd
    sessionid = request.session.get("sessionid","NOSessionID")
    if sessionid == "NOSessionID" :#not logged in                        
        if request.method == "POST": #do login and show the output
            user = int(request.POST["F_RegId"])
            #pwd = request.POST.get('F_Password', False)
            #user = int(request.POST.get('F_RegId', False))
            pwd = request.POST["F_Password"] 
            print("pwd" , pwd)
            print(user)
            try :
                record = faculty.objects.get(F_Id = user)
            except:
                return render(request,'error2.html')
            if pwd == record.F_Password:
                #generate session id 
                temp = getsessionid()
                #add session token to the database
                request.session["sessionid"] = temp
                sessionid = temp
                AF = activeFaculty.objects.create(F_Id= user,sessionid= sessionid)
                lis = gettfcount(user)
                ddod = getdodata(lis)
                return render(request,'welcome.html', {'record': record,'dodata':ddod , 'publis' : lis})
            else :
                return render(request,'error2.html')
        else:
            return render(request,'login.html')
    else: #verify session id
        #is session id is valid
        F_Id = isSessionIDValid(sessionid)
        record = faculty.objects.get(F_Id = F_Id)
        if  F_Id  != None:
            lis = gettfcount(F_Id)
            ddod = getdodata(lis)
            return render(request, 'welcome.html', {'record':record ,'dodata':ddod , 'publis' : lis})
        else:
            del request.session['sessionid']
            return HttpResponse("Invalid session user logout")
    #elsee show the login page
# @csrf_exempt
# def login(request):
#     sessionid = request.session.get("sessionid","NOSessionID")
#     if sessionid == "NOSessionID" :#not logged in
#         temp = getsessionid()
#         #add session token to the database
#         request.session["sessionid"] = temp
#         sessionid = temp
#         messages = "Session Expired"
#         return render(request, 'home.html', {'messages':messages})
        
        
#     return HttpResponse(sessionid +" <br>logged IN yayy!!!")

@csrf_exempt
def logout(request):
    sessionid = request.session.get("sessionid","NOSessionID")
    if sessionid == "NOSessionID" :#not logged in
        return HttpResponse("Not Logged in")
    else :
        try :
            activeFaculty.objects.get(sessionid=sessionid).delete()
        except:
            pass
        del request.session['sessionid']
        return render(request, 'home.html')

def home1(request):
    return render(request,'home.html')

def welcome(request):
    return render(request, 'welcome.html')


@csrf_exempt
def addpub2form(request) :
    global facpubdict  
    form = faculty_publications()
    #form2 = Pub_Form2()
    sessionid = request.session.get("sessionid","NOSessionID")
    if sessionid == "NOSessionID" :#not logged in 
        response = redirect('/crlogin')
        return response

    else:
        sessionid = request.session.get("sessionid","NOSessionID")
        F_Id = isSessionIDValid(sessionid)
        if request.method == 'POST': 
            form = InputForm(request.POST)
            if form.is_valid():
            # id = int(request.POST["P_Id"])
            # title = request.POST["P_Title"]
            # p_obj = publications.objects.create(P_Id= id,P_Title= title)
                pubid = form.cleaned_data['pubid']
                facultypos = form.cleaned_data['facultypos']
                print(pubid) 
                fpos = facultypos  
                f_obj = pfconnect.objects.create(P_Id= pubid,F_Id = F_Id,F_Pos = fpos)
                #form.save()
            
    #         user_pr = form.save(commit=False)
    #         user_pr.display_picture = request.FILES['display_picture']
    #         file_type = user_pr.display_picture.url.split('.')[-1]
    #         file_type = file_type.lower()
    #         #if file_type not in IMAGE_FILE_TYPES:
    #             #return render(request, 'error.html')
    #         user_pr.save()
    #         return render(request, 'details.html', {'user_pr': user_pr})
                facpubdict = datauti.get_publications_Faculty("")
                response = redirect('/faculty_publications')  
                return response
                return    #HttpResponse("Form saved<a> Go to home</a>")
            else:
                return HttpResponse("Form is not valid")
        
        record = faculty.objects.get(F_Id = F_Id)
        form2 = InputForm()
        context = {"form": form, "record" :record ,'form2' : form2}
        return render(request, 'faculty_publications.html', context)

@csrf_exempt
def facultypublications(request):
    global facpubdict  
    form = faculty_publications()
    #form2 = Pub_Form2()
    sessionid = request.session.get("sessionid","NOSessionID")
    if sessionid == "NOSessionID" :#not logged in 
        response = redirect('/crlogin')
        return response

    else:
        sessionid = request.session.get("sessionid","NOSessionID")
        F_Id = isSessionIDValid(sessionid)
        if request.method == 'POST':
            form = faculty_publications(request.POST, request.FILES)
            
            if form.is_valid():
            # id = int(request.POST["P_Id"])
            # title = request.POST["P_Title"]
            # p_obj = publications.objects.create(P_Id= id,P_Title= title)
                post = form.save(commit=False)
                iN = random.randint(0,9999999)
                print("iN", iN)
                fpos = post.P_Id
                post.P_Id = iN
                #post.published_date = timezone.now()
                post.save()
                f_obj = pfconnect.objects.create(P_Id= iN,F_Id = F_Id,F_Pos = fpos)
                #form.save()
            
    #         user_pr = form.save(commit=False)
    #         user_pr.display_picture = request.FILES['display_picture']
    #         file_type = user_pr.display_picture.url.split('.')[-1]
    #         file_type = file_type.lower()
    #         #if file_type not in IMAGE_FILE_TYPES:
    #             #return render(request, 'error.html')
    #         user_pr.save()
    #         return render(request, 'details.html', {'user_pr': user_pr})
                facpubdict = datauti.get_publications_Faculty("")
                response = redirect('/crlogin')
                return response
                return    #HttpResponse("Form saved<a> Go to home</a>")
            else:
                return HttpResponse("Form is not valid")
        
        record = faculty.objects.get(F_Id = F_Id)
        form2 = InputForm()
        context = {"form": form, "record" :record ,'form2' : form2}
        return render(request, 'faculty_publications.html', context)


def welcomeFun(request) :
    sessionid = request.session.get("sessionid","NOSessionID")
    F_Id = isSessionIDValid(sessionid)
    record = faculty.objects.get(F_Id = F_Id)
    if  F_Id  != None:
        print(record)
        return render(request, 'welcome.html', {'record':record})
    else:
        del request.session['sessionid']
        return HttpResponse("Invalid session user logout")


def grpfacpub():

    arrays = []
    print(0)
    names = ('Publication Title', 'Faculty Name','Faculty Position' )
    t = []
    authos = []
    apos = []
    dpos = []
    print(0)
    for key , val in facpubdict.items() : 
        if key  == 'cols' :
            continue
        for v in val:
            titlep = v[3]
            print(v[-1])
            titlep = "<a href=\"/shospub?pid=" +str(v[-1])+"\">" + titlep+ "</a>"
            t.append(titlep)
            authos.append(v[1])
            apos.append(v[2])
            dpos.append(v[9 ])
    arrays = [t,authos,apos]
    print(0)
    index = pd.MultiIndex.from_arrays(arrays, names=names)
    print(0)
    df = pd.DataFrame({'Date of Publication': dpos  },
                    index=index)
        
    print(apos)
    

    return df.to_html(escape=False)
    

def sgrpfacpub(fid):

    arrays = []
    print(0)
    names = ('Publication Title', 'Faculty Name','Faculty Position' )
    t = []
    authos = []
    apos = []
    dpos = []
    print(0)
    val  = facpubdict[fid]
    for v in val:
        titlep = v[3]
        print(v[-1])
        titlep = "<a href=\"/shospub?pid=" +str(v[-1])+"\">" + titlep+ "</a>"
        t.append(titlep)
        authos.append(v[1])
        apos.append(v[2])
        dpos.append(v[9 ])
    arrays = [t,authos,apos]
    print(0)
    index = pd.MultiIndex.from_arrays(arrays, names=names)
    print(0)
    df = pd.DataFrame({'Date of Publication': dpos  },
                    index=index)
        
    print(apos)
    

    return df.to_html(escape=False)
    

def showpublications(request) : 
    flag = False
    try :
        sessionid = request.session.get("sessionid","NOSessionID")
        F_Id = isSessionIDValid(sessionid)
     
        record = faculty.objects.get(F_Id = F_Id)
        if  F_Id  != None:
            print(record)
            cflis = facpubdict[F_Id]
            if len(cflis) != 0:
                userdf = pd.DataFrame(columns=facpubdict['cols'], data=cflis)
                flag = True

 
            userdf = pd.DataFrame(columns=facpubdict['cols'], data=cflis)
            
 
        
            userdata_html = userdf.to_html(escape=False)

            #
            userdata_html = sgrpfacpub(F_Id)
         

            allpubrows = []
            for key , val in facpubdict.items() :
                if key == 'cols' :
                    continue
                allpubrows.extend(val)
       
            alldf = pd.DataFrame(columns=facpubdict['cols'], data=allpubrows)
 
            alldf = alldf.groupby(by=["P_Title"])
            alldf = pd.DataFrame(alldf.size().reset_index(name = "Group_Count"))
            htmlsheet = alldf.to_html(escape=False)  
               
            print('nal')

            htmlsheet = grpfacpub()
            


            return render(request, 'showpublications.html', {'record':record,"uh" : userdata_html, "uall" : htmlsheet ,"flag" : flag })
        else:
            del request.session['sessionid']
            return HttpResponse("Invalid session user logout") 
    except Exception as e :
        print(e)
        return HttpResponse(e) 

def shospub(request) :
    # try : 
    sessionid = request.session.get("sessionid","NOSessionID")
    F_Id = isSessionIDValid(sessionid)
    
    record = faculty.objects.get(F_Id = F_Id) 
    P_Id = request.GET["pid"]
    pubrec = publications.objects.get(P_Id = P_Id)
    fac_names = []
    pfconns = pfconnect.objects.filter(P_Id = P_Id)
    pubs = [] 
    try :
        for pfc in pfconns:
            F_ID = pfc.F_Id
            frec = faculty.objects.get(F_Id = F_ID)
            fac_names.append([frec.F_Name, pfc.F_Pos ,F_ID])
    except :
        pass
    psource = "<a href=\"" +str(pubrec.P_Paper_Source)+"\"> " + str(pubrec.P_Paper_Source)+ "</a>" 
    jsource = "<a href=\"" +str(pubrec.P_Journal_Source)+"\"> " + str(pubrec.P_Journal_Source)+ "</a>" 
    return render(request, 'showpubdet.html', { 'record': record , 'precord': pubrec,'facs' : fac_names ,'dat' : pubrec.P_DOP.strftime("%m/%d/%Y") , 'sou' : psource ,'jso' : jsource})
    # except Exception:
    #     return HttpResponse("Error")