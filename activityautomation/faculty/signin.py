import imp
import re
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import  *
import json
from django.views.decorators.csrf import csrf_exempt
import random
import string
from .signutilities import *








@csrf_exempt
def Cjlogin(request):
    sessionid = request.session.get("sessionid","NOSessionID")
    if sessionid == "NOSessionID" :#not logged in
        temp = getsessionid()
        request.session["sessionid"] = temp
        sessionid = temp
        
    
    return HttpResponse(sessionid)





    if request.method == "POST": #do login and show the output
        print(request.body.decode("utf-8"))
        cred = json.loads(request.body)
        # return HttpResponse(cred["uname"])
        try:
            uname = cred["uname"]
            password = cred["password"]
            if uname != None:

                record = faculty.objects.get(F_RegId=uname)
                if record != None:
                    data = {}
                    tempd = {}
                    templist = []
                    if password == record.cpass:
                        tempd["status"] = "success"
                        # generating a new session id
                        tempd["sessionid"] = getsessionid()


                        #put the session id and F_Id into facultyactivee
                        #save the session id into cookies or session variables
                        #redirect to succesfull page

                    else:
                        #wrong credentials go to login page

                        tempd["status"] = "Incorrect"
                    templist.append(tempd)
                    data["loginproducts"] = templist
                    return JsonResponse(tempd)
                else:
                    return HttpResponse("error")
                data = {}
                tempd = {}
                templist = []
                #tempd["lid"] = record.lid
                tempd["uname"] = record.uname
                tempd["password"] = record.password

                templist.append(tempd)
                data["loginproducts"] = templist
                return JsonResponse(data)

        except:

            return HttpResponse("error")
    #elsee show the login page


user=''
pwd=''
@csrf_exempt
def crlogin(request):
    global user,pwd
    sessionid = request.session.get("sessionid","NOSessionID")
    if sessionid == "NOSessionID" :#not logged in                        
        if request.method == "POST": #do login and show the output
            user = int(request.POST["F_RegId"])
            pwd = request.POST["F_Password"] 
            print("pwd" , pwd)
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
                return render(request,'welcome.html')
            else :
                return render(request,'error2.html')
        else:
            return render(request,'login.html')
    else: #verify session id
        #is session id is valid
        F_Id = isSessionIDValid(sessionid)
        if  F_Id  != None:
            record = faculty.objects.get(F_Id = F_Id)

            return HttpResponse("Logged in as : "+str(record.F_Name))
        else:
            del request.session['sessionid']
            return HttpResponse("Invalid session user logout")



    #elsee show the login page




    
@csrf_exempt
def login(request):
    sessionid = request.session.get("sessionid","NOSessionID")
    if sessionid == "NOSessionID" :#not logged in
        temp = getsessionid()
        #add session token to the database
        request.session["sessionid"] = temp
        sessionid = temp
        return HttpResponse("Not logged in ")
        
        
    return HttpResponse(sessionid +" <br>logged IN yayy!!!")

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
        return HttpResponse("Succesfullly Logged out")

        
    
    return HttpResponse(sessionid)