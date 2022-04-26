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
import os

from django.shortcuts import redirect
import pandas as pd
from django.conf import settings
from IPython.display import HTML

from django.template import loader  


from . import signutilities
srespath = os.path.join(settings.BASE_DIR, 'sres.xlsx')
sheets = ['S1 Student Journal Pub',
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
df2 = pd.read_excel('sres.xlsx',
                 sheets)

sheetsExclude = [  
'S8 Student Events Organized',
 'S9 Student Guest Lectures Organ',
 'S10 Student Prof. Body',
  'S12 Student capabilities enhanc' 


]
def showact(request) : 
    sessionid = request.session.get("sessionid","NOSessionID")
    S_Id = isSessionIDValid(sessionid)
    record = student.objects.get(S_Id = S_Id)
    if  S_Id  != None:
        print(record)
        aurl = str(request.build_absolute_uri())
        url  = aurl.split("/")[-1].replace("_" ," ") #accesed sheet name
        flag = False
        actsheet = df2[url]
        print(type(actsheet))
        htmlsheet = actsheet.to_html() # all the data 
        options = [record.S_RegId] 
        userdata_html = htmlsheet
        if url not in sheetsExclude : 
            flag = True
            user_data = actsheet[ actsheet['Roll Number'].isin(options) ]
            userdata_html = user_data.to_html()
    
       
        return  render(request, 'showactivity.html', {'url':url, "uh" : userdata_html, "uall" : htmlsheet , "record" : record , "flag" : flag})


        return HttpResponse("showing <H1>"+ url+ "</h1> <br><br>" + userdata_html  +"<br> <H2>All Users Data</H2><br>" + htmlsheet + "<br>")
    else:
        del request.session['sessionid']
        return HttpResponse("Invalid session user logout")
    