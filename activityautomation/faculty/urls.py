from django.urls import path
from . import views

from . import signin
from activityautomation import settings
from django.conf.urls.static import static
urlpatterns = [
   # path('', views.hello, name='hello'),

    path('', signin.home1, name='home1'),
    path('importpublicationData', views.importpublicationData, name='importpublicationData'),
    path('viewFaculty', views.viewFaculty ,name='viewFaculty'),
    path('pdfgenerate', views.pdfgenerate ,name='pdfgenerate'),
    path('upload', views.create_profile,name='upload'),
    path('jso', views.jso,name='jso'),
    # path('products', views.products,name='jso'),
    
    
    path('menu', views.menu,name='menu'),


    # path('login', signin.login,name='login'),
    path('logout', signin.logout,name='logout'),
    path('crlogin', signin.crlogin,name='loginform'),
    path('home1', signin.home1,name='homepage'),
    path('welcome', signin.welcome,name='welcome'),
    path('faculty_publications', signin.facultypublications,name='facultypublications'),
    path('showpublications', signin.showpublications,name='showpublications'),


    path('rwel', signin.welcomeFun,name='rwel')
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.BASE_DIR)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)