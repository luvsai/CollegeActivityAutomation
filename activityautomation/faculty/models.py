import datetime
from django.db import models
from datetime import datetime


# Create your models here.
class dummy(models.Model):
    id = models.IntegerField(default=False,primary_key=True)
    key_t = models.CharField(default=False ,max_length=10)
    value_t = models.CharField(default= False,max_length=100)
    dob = models.CharField(default= False,max_length=100)#models.DateTimeField(default=False)
 
    def __str__(self):
        return self.title

    class Meta:
        db_table = "dummmy"

class publications(models.Model):
    P_Id = models.IntegerField(default=False, verbose_name="Publication ID", primary_key=True)
    P_Title = models.CharField(default=False, verbose_name="Publication Title", max_length=500)
    P_Joural_Name = models.CharField(default=False, verbose_name="Journal Name", max_length=500)
    P_Indexing = models.CharField(default=False, verbose_name="Indexing", max_length=45)
    P_IF_State = models.CharField(default=False, verbose_name="Impact Factor State", max_length=100)
    P_IF_Value  = models.CharField(default=False, verbose_name="Impact Factor Value", max_length=20)
    P_IF_Source = models.CharField(default=False, verbose_name="Impact Facotr Source", max_length=20)
    P_DOP = models.DateTimeField(verbose_name="Date of Publications")#models.DateTimeField(default=False)
    P_DOI = models.CharField(default=False, verbose_name="DOI",max_length=250)
    P_Page_Nos = models.CharField(default=False, verbose_name="Number of Pages", max_length=45)
    P_ISSN = models.CharField(default=False, verbose_name="ISSN", max_length=45)
    P_Volume = models.CharField(default=False, verbose_name="Volume", max_length=20)
    P_Issue = models.CharField(default=False, verbose_name="Issue", max_length=20)
    P_Journal_Source = models.CharField(default=False, verbose_name="Journal Source", max_length=500)
    P_Paper_Source = models.FileField(default=False, verbose_name="Paper Source",  max_length=500)


    class Meta:
        db_table = "publications"


class faculty(models.Model) :
    F_Id = models.IntegerField(default=False,primary_key=True)
    F_Name = models.CharField(default=False ,max_length=100)
    F_Email = models.CharField(default=False ,max_length=100)
    F_Mob = models.CharField(default=False ,max_length=10)
    F_Password = models.CharField(default=False ,max_length=45)
    F_Dept = models.CharField(default=False ,max_length=45)
    F_RegId = models.CharField(default=False ,max_length=45)


    class Meta:
        db_table = "faculty"


class User_Profile(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length = 200)
    technologies = models.CharField(max_length=500)
    email = models.EmailField(default = None)
    display_picture = models.FileField()
    def __str__(self):
        return self.fname

class activeFaculty(models.Model):
    A_Id = models.IntegerField(primary_key=True)
    F_Id = models.IntegerField()
    sessionid = models.CharField(
        default="sadbfahfdsfhhKJHeehhOHugu", max_length=200)

    class Meta:
        db_table = "activefaculty"