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
        