import random
import string
from tkinter.messagebox import RETRY
from .models import *
from django.shortcuts import render
def getsessionid():
    S = 20  # number of characters in the string.
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    return str(ran)

def isSessionIDValid(sessionid): # if valid  return F_Id
    try :
        record = activeFaculty.objects.get(sessionid = sessionid)
        return record.F_Id
    except:
        return None
