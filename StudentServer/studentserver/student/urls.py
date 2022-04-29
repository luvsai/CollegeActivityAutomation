from pyexpat import features
from django.urls import path

from . import stufes

from . import signin , data ,stufes
from . import views
from django.conf.urls.static import static
from studentserver import settings
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
 'S18 Students Placements','S1: Student Journal Pub',
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
urlpatterns = [
   

    path('', signin.home1, name='home1'),
    #path('importpublicationData', views.importpublicationData, name='importpublicationData'),
    path('viewStudent', views.viewStudent ,name='viewStudent'),
   # path('pdfgenerate', views.pdfgenerate ,name='pdfgenerate'),
    #path('upload', views.create_profile,name='upload'),
    #path('jso', views.jso,name='jso'),
    # path('products', views.products,name='jso'),
    
    
   

    # path('login', signin.login,name='login'),
    path('logout', signin.logout,name='logout'),
    path('crlogin', signin.crlogin,name='loginform'),
    path('home1', signin.home1,name='homepage'),
    path('welcome', signin.welcome,name='welcome'),
  #  path('faculty_publications', signin.facultypublications,name='facultypublications'),
    path('showpublications', signin.showpublications,name='showpublications'),


    path('rwel', signin.welcomeFun,name='rwel'),
    path('pie', stufes.piechart,name='pie'),


]
for sheet in sheets :
    s1 = sheet
    sheet = sheet.replace(" ", "_")
    sheet = sheet.replace(":", "-")
    sheet = sheet.replace("/", "~")

    print(sheet)
    urlpatterns.append(  path(sheet, data.showact, name=sheet))
    urlpatterns.append(  path('<str:key>' , data.showact, name=sheet))




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.BASE_DIR)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)