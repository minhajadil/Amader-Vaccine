from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from  .models import VaccineTaken
# Create your views here.
from Doctor.models import Vaccine


@login_required
def take_vaccine(request,id):
    vaccine = get_object_or_404(Vaccine, pk=id)
    taken = False 
    
    
    if VaccineTaken.objects.filter(user=request.user, vaccine=vaccine).exists():
        taken = True 
       
    
    VaccineTaken.objects.create(user=request.user, vaccine=vaccine)

    return redirect('homepage')