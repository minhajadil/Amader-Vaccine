from django.shortcuts import render,redirect
from Doctor.models import Vaccine
from  Patient.models import VaccineTaken

from Blog.models import Posts



    



def homepage(request):

    vaccines = Vaccine.objects.all()
    blogs = Posts.objects.all()
    print(blogs)
   

    if request.user.is_authenticated:
        doctor = False 
        has_edit_access = False 
        account_type = request.user.account.account_type
       
        if account_type == 'doctor':
            doctor=True 
            
        return render(request, 'homepage.html',{'has_edit_access':has_edit_access,'doctor':doctor,'vaccines':vaccines,'blogs':blogs})
    else :
        return render(request,'homepage.html',{'vaccines':vaccines,'blogs':blogs})
    

   