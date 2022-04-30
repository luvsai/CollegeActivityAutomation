from os import P_PID
import random
import string
from tkinter.messagebox import RETRY
from .models import *
from django.shortcuts import render




def get_publications_Faculty(x) :
    facultyrs = faculty.objects.all()
    facpubdic = {}
    facpubdic ['cols'] =['FacultyID','Faculty Name','Faculty_Position','P_Title' ,
                    'P_Joural_Name'  ,
                    'P_Indexing'  ,
                    'P_IF_State' ,
                    'P_IF_Value'  ,
                    'P_IF_Source' ,
                    'P_DOP' ,
                    'P_DOI' ,
                    'P_Page_Nos' ,
                    'P_ISSN' ,
                    'P_Volume' ,
                    'P_Issue' ,
                    'P_Journal_Source' ,
                    'P_Paper_Source','Publication ID' ]
    print(facpubdic)
    for fac in facultyrs :
        F_ID = fac.F_Id
        pfconns = pfconnect.objects.filter(F_Id = F_ID)
        pubs = [] 
        try :
            frec = faculty.objects.get(F_Id = F_ID)
            for record in pfconns :
                publi = publications.objects.get(P_Id = record.P_Id)
                pubs.append([  F_ID, frec.F_Name , record.F_Pos  ,publi.P_Title, publi.P_Joural_Name , publi.P_Indexing, publi.P_IF_State,publi.P_IF_Value,
                publi.P_IF_Source, publi.P_DOP.strftime("%m/%d/%Y"),publi.P_DOI, 
                publi.P_Page_Nos, publi.P_ISSN,publi.P_Volume, 
                publi.P_Issue, publi.P_Journal_Source,"<a href=\"" +str(publi.P_Paper_Source)+"\"> " + str(publi.P_Paper_Source)+ "</a>", publi.P_Id
                ])
            facpubdic[F_ID]=pubs
        except :
            continue


    
    return facpubdic
        
 