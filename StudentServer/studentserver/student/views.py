from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
 
from .models import *

import datetime
import random
import json


from django.conf import settings
import os
from django.template import loader  

# Create your views here.
def shome(request):

    return HttpResponse("Student server home")


def viewStudent(request) : 
    
    objects = student.objects.all()
     
    res ='Printing all Dummmy entries in the DB : <br>'
    
     
    parsedata = {}
    data = []
    for rec in objects:
        data.append([rec.S_RegId , rec.S_Name])
    parsedata["data"] = data

    
    
    
    template = loader.get_template('students.html')


     
    #jsonoutput = json.dumps(parsedata, indent=4)

    
    #return JsonResponse(parsedata)
    
     # getting our template  
    return HttpResponse(template.render(parsedata))

