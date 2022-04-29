
from operator import imod
from pydoc import safeimport
from random import Random
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse  
# Create your views here.

from django.views.decorators.http import require_http_methods
from parso import parse  
from faculty.models import dummy , publications , faculty ,Products

import datetime
import random
import json


from django.conf import settings
import os
from django.template import loader  

from .forms import Profile_Form
from .models import  User_Profile





#---------------------------



# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = publications_table_from_dict(json.loads(json_string))

from enum import Enum
from datetime import datetime
from typing import Union, Any, List, TypeVar, Type, Callable, cast
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


 


class PublicationsTableElement:
    col1: int
    col2: str
    col3: str
    col4: str
    col5: str
    col6: str
    col7: str
    col8: datetime
    col9: str
    col10: str
    col11: str
    col12: str
    col13: str
    col14: str
    col15: str

    def __init__(self, col1: int, col2: str, col3: str, col4: str, col5: str, col6: str, col7: str, col8: datetime, col9: str, col10: str, col11: str, col12: str, col13: str, col14: str, col15: str) -> None:
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3
        self.col4 = col4
        self.col5 = col5
        self.col6 = col6
        self.col7 = col7
        self.col8 = col8
        self.col9 = col9
        self.col10 = col10
        self.col11 = col11
        self.col12 = col12
        self.col13 = col13
        self.col14 = col14
        self.col15 = col15

    @staticmethod
    def from_dict(obj: Any) -> 'PublicationsTableElement':
        assert isinstance(obj, dict)
        col1 = int(from_str(obj.get("col1")))
        col2 = from_str(obj.get("col2"))
        col3 = from_str(obj.get("col3"))
        col4 = from_str(obj.get("col4"))
        col5 = from_str(obj.get("col5"))
        col6 = from_str(obj.get("col6"))
        col7 = from_str(obj.get("col7"))
        col8 = from_datetime(obj.get("col8"))
        col9 = from_str(obj.get("col9"))
        col10 = from_str(obj.get("col10"))
        col11 = from_str(obj.get("col11"))
        col12 = from_str(obj.get("col12"))
        col13 = from_str(obj.get("col13"))
        col14 = from_str(obj.get("col14"))
        col15 = from_str(obj.get("col15"))
        return PublicationsTableElement(col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15)

    def to_dict(self) -> dict:
        result: dict = {}
        result["col1"] = from_str(str(self.col1))
        result["col2"] = from_str(self.col2)
        result["col3"] = from_str(self.col3)
        result["col4"] = from_str(self.col4)
        result["col5"] = from_str( self.col5)
        result["col6"] = from_str( self.col6)
        result["col7"] = from_str(self.col7)
        result["col8"] = self.col8.isoformat()
        result["col9"] = from_str(self.col9)
        result["col10"] = from_str(self.col10)
        result["col11"] = from_str(self.col11)
        result["col12"] =  from_str( self.col12)
        result["col13"] = from_str(self.col13)
        result["col14"] = from_str(self.col14)
        result["col15"] = from_str(self.col15)
        return result


def publications_table_from_dict(s: Any) -> List[PublicationsTableElement]:
    return from_list(PublicationsTableElement.from_dict, s)


def publications_table_to_dict(x: List[PublicationsTableElement]) -> Any:
    return from_list(lambda x: to_class(PublicationsTableElement, x), x)


#---------------------------





def hello(request) :

    response = """{ "hello" : "user"}"""
    dic = {"hello" : "User"}
    # creating an instance of 
    # datetime.date
    #d = datetime.datetime.now()
    #datetime1= datetime.datetime(year=2016,month=12,day=1)
    
    # creating an instance of 
    # 
    #dummy_object = dummy.objects.create(id = random.randint(1000,10044),dob = "2099-09-01",key_t = "lavanya sai kumar")
    #dummy_object.save()
    objects = dummy.objects.all()
    res ='Printing all Dummmy entries in the DB : <br>'
    
  #  for elt in objects:
   #     x = ""
    #    if (elt.dob != None): 
     #       x = str(elt.dob)
      #  res += str(elt.id) + " : " +elt.key_t+ " : " + elt.value_t + " : "+ x + "<br>"

    

    id = int(request.GET["fid"])
    record = faculty.objects.get(F_Id = id)

    data = {}
    data["F_Id"] = record.F_Name
    
    res += str(record.F_Name) + "<br>"


    
    return JsonResponse(data)
    return HttpResponse(res+ "<br>")
    return HttpResponse(res + "<br><br>" )




 

def importpublicationData(request) :
    
    #return HttpResponse("OK")


    file_ = open(os.path.join(settings.BASE_DIR, '1718.json'), "r")
    
    #read whole file to a string
    data = file_.read()
    result = publications_table_from_dict(json.loads(data))
    print(result)
    #close file
    file_.close()
 
 
    print(len(result))


    j = 0
    for i in range(0,len(result)) :
    #trying toinsert a publication obj
        try :
            print()
            publication_obj = publications.objects.create(P_Id= int(result[i].col1),P_Title = result[i].col2,
            P_Joural_Name = result[i].col3 ,
            P_Indexing = result[i].col4,
            P_IF_State= result[i].col5,
            P_IF_Value= result[i].col6,
            P_IF_Source= result[i].col7,
            P_DOP= result[i].col8,
            P_DOI= result[i].col9,
            P_Page_Nos= result[i].col10,
            P_ISSN= result[i].col11,
            P_Volume= result[i].col12,P_Issue= result[i].col13,
            P_Journal_Source= result[i].col14,P_Paper_Source= result[i].col15) 
        
            publication_obj.save()
        except :
            print(result[i].col5)
            j+=1
         

    print("Data Imported : " , j)



    return HttpResponse("<H1> DaTA Import Success OK!!!</H!>"+ "<br><br>"  + str(j) )

    





def viewFaculty(request) :
    
    
    
    
    
    objects = faculty.objects.all()
    




    res ='Printing all Dummmy entries in the DB : <br>'
    
     
    parsedata = {}
    data = []
    for rec in objects:
        data.append([rec.F_Id , rec.F_Name])
    parsedata["data"] = data

    
    
    
    template = loader.get_template('faculty.html')


     
    #jsonoutput = json.dumps(parsedata, indent=4)

    
    #return JsonResponse(parsedata)
    
# # getting our template  
    return HttpResponse(template.render(parsedata))





from reportlab.pdfgen import canvas  

def pdfgenerate(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response,initialFontSize=5)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Faculty Data.")  
    objects = faculty.objects.all()
    strin = ""
    for rec in objects:
        strin += str(rec.F_Id) + " : " + str(rec.F_Name ) + "\n"
       
        print(rec.F_Id)
    
    print(strin)
    p.drawString(100,800, strin) 
    p.showPage()  
    p.save()  
    return response  


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
def create_profile(request):
    form = Profile_Form()
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            #if file_type not in IMAGE_FILE_TYPES:
                #return render(request, 'error.html')
            user_pr.save()
            return render(request, 'details.html', {'user_pr': user_pr})
    context = {"form": form,}
    return render(request, 'create.html', context)



def jso(request) :
    x = { "id " : 123}

    return JsonResponse(x)


def menu(request):
    menu = {
               "menudata": {
                    "id": "13",
                    "name": "Cappuccino",
                    "price" :  {
                        200 : "500RS",
                        400 : "600Rs"
                    },
                    "extras" : ["cake", "jellytart"]
                    
                }
   

        }


    template = loader.get_template('menu.html')


    
    return HttpResponse(template.render(menu))




    return HttpResponse(menu)


def home(request):


    strres = """<!DOCTYPE html>
<html>
<body>

<h2>An ordered HTML list</h2>

<ol>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>  

</body>
</html>

"""

    return HttpResponse(strres)













def products(request):
    objects = Products.objects.all()
    




    res ='Printing all Product entries in the DB : <br>'
    
     
    parsedata = {}
    product = []
    for rec in objects:
        product.append([rec.pid , rec.pname])
    parsedata["products"] = product

    
    
    return JsonResponse(parsedata)
    template = loader.get_template('faculty.html')
    
    
    
    return HttpResponse("{ \"pid\" :1234 ,\"pname\" : \"Santoor Mommy\"}")
    pass







