from django import forms
from .models import Vaccine

class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['name','initial_dose' , 'images']

        widgets = {
            'initial_dose': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean_initial_dose(self):
        initial_dose = self.cleaned_data['initial_dose']
        return initial_dose
    
class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
