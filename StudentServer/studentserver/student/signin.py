import imp
import re
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import  *
import json
from django.views.decorators.csrf import csrf_exempt
import random
import string
from .signutilities import *
 

from django.shortcuts import redirect

user=''
pwd=''


sheets =  ['S1 Student Journal Pub',
					'S2 Student Conference Publicati',
					'S3 Student Internships',
					'S4 Student Certifications',
					'S5 Student WorkshopsConf attend',
					'S6 Student NPTEL',
					'S7 Student Workshops Organized',
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

for sheet in sheets:
    sdic [sheet] = sheet.replace(" ", "_")
print(sdic)
@csrf_exempt
def crlogin(request):
    global user,pwd
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
                    sessionid = temp
                    AF = activeStudent.objects.create(S_Id= record.S_Id ,sessionid= sessionid)

                    return render(request,'welcome.html', {'record': record ,'sheets': sheets , 'sdic' : sdic})
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
            return render(request, 'welcome.html', {'record':record ,'sheets': sheets, 'sdic' : sdic})
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