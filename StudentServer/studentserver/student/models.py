from django.db import models

# Create your models here.

class student(models.Model) :
    S_Id = models.IntegerField(default=False,primary_key=True)
    S_Name = models.CharField(default=False ,max_length=100)
    S_Email = models.CharField(default=False ,max_length=100)
    S_Mob = models.CharField(default=False ,max_length=10)
    S_Password = models.CharField(default=False ,max_length=45)
    S_Dept = models.CharField(default=False ,max_length=45)
    S_RegId = models.CharField(default=False ,max_length=45)
    S_Sec = models.CharField(default=False ,max_length=45)


    class Meta:
        db_table = "student"
class activeStudent(models.Model):
    A_Id = models.IntegerField(primary_key=True)
    S_Id = models.IntegerField()
    sessionid = models.CharField(
        default="sadbfahfdsfhhKJHeehhOHugu", max_length=200)

    class Meta:
        db_table = "activeStudent"