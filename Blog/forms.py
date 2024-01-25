from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    content= forms.CharField(widget=forms.TextInput(attrs={'class': 'content-form'}))
    class Meta :
        model =Posts
        fields =['title','content','category','image']