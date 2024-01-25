from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms



class PatientRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    nid = forms.CharField(required=True)
    class Meta :
        model = User
        fields=['username','first_name','last_name','email','nid']

class DoctorRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta :
        model = User
        fields=['username','first_name','last_name','email']


class datachange(UserChangeForm):
    password= None 
    class Meta :
        model = User
        fields=['username','first_name','last_name','email']



