from django.urls import path
from . import views

from . import signin
from activityautomation import settings
from django.conf.urls.static import static
urlpatterns = [
   # path('', views.hello, name='hello'),

    path('', views.home, name='home'),
    path('importpublicationData', views.importpublicationData, name='importpublicationData'),
    path('viewFaculty', views.viewFaculty ,name='viewFaculty'),
    path('pdfgenerate', views.pdfgenerate ,name='pdfgenerate'),
    path('upload', views.create_profile,name='upload'),
    path('jso', views.jso,name='jso'),
    path('products', views.products,name='jso'),

    
    path('menu', views.menu,name='menu'),

     path('login', signin.crlogin,name='login'),
     path('logout', signin.logout,name='logout'),

      path('hello', views.hello,name='logout'),



    
   
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.BASE_DIR)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)