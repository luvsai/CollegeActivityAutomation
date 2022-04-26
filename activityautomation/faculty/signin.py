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
from .forms import faculty_publications, Profile_Form

from django.shortcuts import redirect

user=''
pwd=''
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
                return render(request,'welcome.html', {'record': record})
            else :
                return render(request,'error2.html')
        else:
            return render(request,'login.html')
    else: #verify session id
        #is session id is valid
        F_Id = isSessionIDValid(sessionid)
        record = faculty.objects.get(F_Id = F_Id)
        if  F_Id  != None:
            return render(request, 'welcome.html', {'record':record})
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

def facultypublications(request):
    form = faculty_publications()
    if request.method == 'POST':
        form = faculty_publications(request.POST, request.FILES)
        sessionid = request.session.get("sessionid","NOSessionID")
        F_Id = isSessionIDValid(sessionid)
        if form.is_valid():
        # id = int(request.POST["P_Id"])
        # title = request.POST["P_Title"]
        # p_obj = publications.objects.create(P_Id= id,P_Title= title)
            post = form.save(commit=False)
            iN = random.randint(0,9999999)
            print("iN", iN)
            post.P_Id = iN
            #post.published_date = timezone.now()
            post.save()
            f_obj = pfconnect.objects.create(P_Id= iN,F_Id = F_Id,F_Pos = 0)
            #form.save()
        
#         user_pr = form.save(commit=False)
#         user_pr.display_picture = request.FILES['display_picture']
#         file_type = user_pr.display_picture.url.split('.')[-1]
#         file_type = file_type.lower()
#         #if file_type not in IMAGE_FILE_TYPES:
#             #return render(request, 'error.html')
#         user_pr.save()
#         return render(request, 'details.html', {'user_pr': user_pr})
            response = redirect('/rwel')
            return response
            return    #HttpResponse("Form saved<a> Go to home</a>")
        else:
            return HttpResponse("Form is not valid")
    context = {"form": form,}
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


def showpublications(request) : 
    return HttpResponse("showing publications of a user")