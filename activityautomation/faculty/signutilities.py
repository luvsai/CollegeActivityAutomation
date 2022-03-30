import random
import string

def getsessionid():
    S = 20  # number of characters in the string.
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    return str(ran)

def isSessionIDValid(sessionid):
    
    pass