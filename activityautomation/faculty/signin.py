import imp
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import  *
import json
from django.views.decorators.csrf import csrf_exempt
import random
import string
from .signutilities import *



@csrf_exempt
def login(request):
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

    
