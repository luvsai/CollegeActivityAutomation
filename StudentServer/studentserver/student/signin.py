from dataclasses import dataclass
import imp
import re
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from  .gsheets import getSheetdf
from .models import  *
import json
from django.views.decorators.csrf import csrf_exempt
import random
import string
from .signutilities import *
 

from django.shortcuts import redirect
import pandas as pd
import threading
import time
user=''
pwd=''
import os

esheets =  ['S1 Student Journal Pub',
					'S2 Student Conference Publicati',
					'S3 Student Internships',
					'S4 Student Certifications',
				'S5 Student WorkshopsConf attend',
					'S6 Student NPTEL',
				#	'S7 Student Workshops Organized',
					'S8 Student Events Organized',
					'S9 Student Guest Lectures Organ',
					'S10 Student Prof. Body',
					'S11 Student Awards',
					'S12 Student capabilities enhanc',
					'S13 Students Higher Edu.',
					'S14 Students Competitive Exams',
					'S15 Students Industry Visit',
					'S16 Students Social Service Pro',
					'S17 Students Leadership & Volun',
					'S18 Students Placements']

sdic = {}
file_s = open(os.path.join(settings.BASE_DIR, 'sres4.xlsx'), "r")
 
df2 = pd.read_excel(file_s,
                 esheets)
 


esheetsExclude = [   'S7 Student Workshops Organized',
'S8 Student Events Organized',
 'S9 Student Guest Lectures Organ',
 'S10 Student Prof. Body',
  'S12 Student capabilities enhanc' 


]


#-----gsheets
sheets = ['S1: Student Journal Pub',
 'S2: Student Conference Publication', 
 'S3: Student Internships',
  'S4: Student Certifications',
  'S5: Student Workshops/Conf attended',
    'S6: Student NPTEL', 
#    'S7: Student Workshops Organized',
    'S8: Student Events Organized',
     'S9: Student Guest Lectures Organized',
      'S10: Student Prof. Body', 
      'S11: Student Awards',
       'S12: Student capabilities enhancement', 
       'S13: Students Higher Edu.', 
       'S14: Students Competitive Exams',
 'S15: Students Industry Visit',
  'S16: Students Social Service Programs',
   'S17: Students Leadership & Volunteering Activities', 
   'S18: Students Placements']

sheetsExclude = [   
    # 'S7: Student Workshops Organized',
  'S8: Student Events Organized',
     'S9: Student Guest Lecutres Organized',
     'S10: Student Prof. Body', 
   'S12: Student capabilities enhancement'


]
#---


nsheets = []


count = 1
#-----------------function to load the data sheet from the google sheets into memory


memorysheets = {}




#print(sdic)
def loadStats(RegId=""):
    global nsheets
    nsheets = []
    sdict = {}
    for i in range(len(sheets)):
        actsheet = memorysheets[sheets[i]]
        if actsheet is  None:
            actsheet = df2[esheets[i]]
            u = 0
            all = actsheet.shape[0]
            if esheets[i] not in esheetsExclude :
                try :
                    actsheet = actsheet.sort_values(by=['Roll Number'], ascending=True)
                    actsheet['Roll Number'] = actsheet['Roll Number'].map( str)
                    actsheet['Roll Number'] = actsheet['Roll Number'].map( str.upper)
                    

                    options = [RegId]  
                    user_data = actsheet[ actsheet['Roll Number'].isin(options) ] 
                    u = user_data.shape[0]
                except:
                    pass
            print(esheets[i])
            href = esheets[i].replace(" ", "_")
            href = href.replace(":", "-")
            href = href.replace("/", "~")
            sdict [esheets[i]] = [href, all, u]

            nsheets.append(esheets[i])
            print(href)
            continue
        u = 0
        all = actsheet.shape[0]
        if sheets[i] not in sheetsExclude :
            try :
                actsheet = actsheet.sort_values(by=['Roll Number'], ascending=True)
                actsheet['Roll Number'] = actsheet['Roll Number'].map( str)
                actsheet['Roll Number'] = actsheet['Roll Number'].map( str.upper)
                

                options = [RegId]  
                user_data = actsheet[ actsheet['Roll Number'].isin(options) ] 
                u = user_data.shape[0]
            except:
                pass
        print(sheets[i])
        
        href = sheets[i].replace(" ", "_")
        href = href.replace(":", "-")
        href = href.replace("/", "~")
        sdict [sheets[i]] = [href, all, u]
        print(href)
        nsheets.append( sheets[i])
    #print(sdict)
    sdic = sdict
    return sdict

piedata = [
  
  ['Student Activities', 'Count']
  
]

def addPieData(sdict) :
    piedat = piedata[:]
    for key ,value in sdict.items() :
        piedat.append([key , value[2]])
    return piedat









#---top students 
topstu = []


def loadallstu() :
    allstudata = []
    global topstu
    
    print("Computing top students")
    objs = student.objects.all()
    for rec in objs: 
        sdict = loadStats(rec.S_RegId)
        count = 0
        for values in sdict.values():
            count += values[2]
        allstudata.append([rec.S_RegId, rec.S_Name, rec.S_Email,count])
    stop = pd.DataFrame(columns=['RID','NAME','EMAIL','COUNT'], data=allstudata)
    stop = stop.sort_values(by=['COUNT'], ascending=False)
    tops = stop.head(n=10)
    print(tops)
    Row_list =[]
  
    # Iterate over each srow
    rank = 1
    for index, rows in tops.iterrows():
        # Create list for the current row
        my_list =[rows.RID, rows.NAME, rows.EMAIL, rows.COUNT,rank]
        rank += 1
        # append the list to the final list
        Row_list.append(my_list)
    topstu = Row_list
    print(topstu)
    








def loadsheets() :
    global count
    while True:
        print("signin.py: ++++++loading sheets started : Count : --->>>" ,count)
        for i in range(len(sheets)):
            actsheet = getSheetdf(sheets[i])
            memorysheets[sheets[i]] = actsheet
        print("signin.py: ------loading sheets completed : Count : --->>>" ,count)
        loadallstu()
        count +=1
        time.sleep(30)


       


t1 = threading.Thread(target=loadsheets)
t1.start()



#------

















@csrf_exempt
def crlogin(request):
    global user,pwd  , nsheets ,topstu
    sessionid = request.session.get("sessionid","NOSessionID")
    if sessionid == "NOSessionID" :#not logged in                        
        if request.method == "POST": #do login and show the output
            user = str(request.POST["S_RegId"])
            #pwd = request.POST.get('F_Password', False)
            #user = int(request.POST.get('F_RegId', False))
            pwd = request.POST["S_Password"] 
            print("pwd" , pwd)
            print(user)
            try :
                record = student.objects.get(S_RegId = user)
                print(1)
                if pwd == record.S_Password:
                    #generate session id 
                    temp = getsessionid()
                    print(2)
                    #add session token to the database
                    request.session["sessionid"] = temp
                    print(2)
                    sessionid = temp
                    print(3)
                    AF = activeStudent.objects.create(S_Id= record.S_Id ,sessionid= sessionid)
                    print(4)
                    sdict = loadStats(RegId=record.S_RegId)
                    piedat =  addPieData(sdict)
                    print(5)
                    print(topstu)

                    return render(request,'welcome.html', {'record': record ,'sheets': nsheets , 'sdic' : sdict, 'piedata' : piedat,'topstu' : topstu})
                else :
                    return render(request,'error2.html')
            except:
                return render(request,'error2.html')
            
        else:
            return render(request,'login.html')
    else: #verify session id
        #is session id is valid
        S_Id = isSessionIDValid(sessionid)
        record = student.objects.get(S_Id = S_Id)
        if  S_Id  != None:
            sdict = loadStats(RegId=record.S_RegId)
            piedat =  addPieData(sdict)
            print(topstu)
            return render(request,'welcome.html', {'record': record ,'sheets': nsheets , 'sdic' : sdict, 'piedata' : piedat , 'topstu' : topstu})
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
            activeStudent.objects.get(sessionid=sessionid).delete()
        except:
            pass
        del request.session['sessionid']
        return render(request, 'home.html')

def home1(request):
    return render(request,'home.html')

def welcome(request):
    return render(request, 'welcome.html')

def welcomeFun(request) :
    sessionid = request.session.get("sessionid","NOSessionID")
    S_Id = isSessionIDValid(sessionid)
    record = student.objects.get(S_Id = S_Id)
    if  S_Id  != None:
        print(record)
        return render(request, 'welcome.html', {'record':record})
    else:
        del request.session['sessionid']
        return HttpResponse("Invalid session user logout")


def showpublications(request) : 
    return HttpResponse("showing publications of a user")


def showact(request) : 
    return HttpResponse("showing publications of a user")