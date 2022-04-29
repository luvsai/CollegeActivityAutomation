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
import os

from django.shortcuts import redirect
import pandas as pd
from django.conf import settings
from IPython.display import HTML

from django.template import loader  
import time
from django.conf import settings
from . import signutilities
srespath = os.path.join(settings.BASE_DIR, 'sres.xlsx')

import threading

from . import signin



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


# file_s = os.path.join(settings.BASE_DIR, 'sres4.xlsx')
 
# df2 = pd.read_excel(file_s,
#                  sheets, engine='openpyxl')

sheetsExclude = [   'S7 Student Workshops Organized',
'S8 Student Events Organized',
 'S9 Student Guest Lectures Organ',
 'S10 Student Prof. Body',
  'S12 Student capabilities enhanc' 


]



#-----gsheets
sheets  = ['S1: Student Journal Pub',
 'S2: Student Conference Publication', 
 'S3: Student Internships',
  'S4: Student Certifications',
   'S5: Student Workshops/Conf attended', 'S6: Student NPTEL', 
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
    #  'S7: Student Workshops Organized',
  'S8: Student Events Organized',
     'S9: Student Guest Lecutres Organized',
      'S10: Student Prof. Body', 
   'S12: Student capabilities enhancement'


]
#---
count = signin.count
#-----------------function to load the data sheet from the google sheets into memory
memorysheets = {}
def loadsheets() :
    global count
    while True:
        print("data.py: ++++++loading sheets started : Count : --->>>" ,count)
        for i in range(len(sheets)):
            actsheet = getSheetdf(sheets[i])
            memorysheets[sheets[i]] = actsheet
        print("data.py: ------loading sheets completed : Count : --->>>" ,count)
        count +=1
        
        time.sleep(30)

        



t1 = threading.Thread(target=loadsheets)
t1.start()





#------



def showact(request,key="") : 
    sessionid = request.session.get("sessionid","NOSessionID")
    S_Id = isSessionIDValid(sessionid)
    record = student.objects.get(S_Id = S_Id)
    if  S_Id  != None:
        print(record)
        aurl = str(request.build_absolute_uri())
        url  = aurl.split("/")[-1].replace("_" ," ") #accesed sheet name
        url = url.replace("-", ":")
        url = url.replace("~", "/")
        flag = False
        #actsheet = df2[url]

        #get sheetdf from googapi
        actsheet = memorysheets[url]
        
        
        print(type(actsheet))
        htmlsheet = actsheet.to_html() # all the data 
        
        options = [record.S_RegId] 
        userdata_html = htmlsheet
        if url not in sheetsExclude : 
            actsheet = actsheet.sort_values(by=['Roll Number'], ascending=True)
            actsheet['Roll Number'] = actsheet['Roll Number'].map( str)
            actsheet['Roll Number'] = actsheet['Roll Number'].map( str.upper)
            htmlsheet = actsheet.to_html() # all the data 
            flag = True
            user_data = actsheet[ actsheet['Roll Number'].isin(options) ]
            userdata_html = user_data.to_html()
    
       
        return  render(request, 'showactivity.html', {'url':url, "uh" : userdata_html, "uall" : htmlsheet , "record" : record , "flag" : flag})


        return HttpResponse("showing <H1>"+ url+ "</h1> <br><br>" + userdata_html  +"<br> <H2>All Users Data</H2><br>" + htmlsheet + "<br>")
    else:
        del request.session['sessionid']
        return HttpResponse("Invalid session user logout")
    