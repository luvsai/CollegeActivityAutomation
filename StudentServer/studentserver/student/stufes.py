from dataclasses import dataclass
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
 

from django.shortcuts import redirect
import pandas as pd
import threading
import time
 
piedata = [
  
  ['Student Activities', 'Count'],
  ['Work', 8],
  ['Eat', 2],
  ['TV', 4],
  ['Gym', 2],
  ['Sleep', 8]
]

@csrf_exempt
def piechart(request):

    return render(request,'pietest.html',{'piedata' :  piedata})