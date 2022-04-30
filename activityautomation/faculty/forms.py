from random import choices
from django import forms
from .models import User_Profile,publications
 
#DataFlair #File_Upload

I_Factor_CHOICES = (
   ('YES', 'Yes'),
   ('NO', 'No')
)
class Profile_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = [
        'fname',
        'lname',
        'technologies',
        'email',
        'display_picture'
        ]

class faculty_publications(forms.ModelForm):
    class Meta:
        model = publications
        fields='__all__'

 
# class Pub_Form2(forms.Form):
#     pubchoices = []
#     I_Factor_CHOICES = (
#    ('Yes', 'Yes'),
#    ('No', 'No'))
#     def __init__(self) :
#         pubrecs = publications.objects.all()
#         for rec in pubrecs:

#             pass    

#     publication = forms.CharField(label='Publication Title', max_length=100  )

pubchoices = []
FPos_cho = [
   (1, '1'),
   (2, '2'),
   (3, '3'),
   (4, '4'),
   (5, '5'),
   (6, '6'),
   (7, '7'),
   (8, '8'),
   (9, '9'),
   (10, '10'),
]
def update():
    global pubchoices
    pubrecs = publications.objects.all()
    pubchoices = []
    for rec in pubrecs :
        pubchoices.append((rec.P_Id, rec.P_Title))
update()
class InputForm(forms.Form): 
    # def __init__(self):
    #     update() 
    #     pubrecs = publications.objects.all()
    #     pubchoices = []
    #     for rec in pubrecs :
    #         pubchoices.append((rec.P_Id, rec.P_Title))
    #     super().__init__()  

    pubid = forms.ChoiceField(label="Publication Title" , choices= pubchoices)
    facultypos = forms.ChoiceField(
                     help_text = "Enter 6 digit roll number"
                     ,label="Author Position In the Publication ",
                     choices = FPos_cho
                     )

    