from django.shortcuts import render, redirect
from .forms import VaccineForm,CommentForm
from .models import Vaccine,Comment
from Account.models import AccountModel
from django.contrib import messages

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from  Patient.models import VaccineTaken




def create_vaccine(request):
    if request.method == 'POST':
        form = VaccineForm(request.POST,request.FILES)
        if form.is_valid():
            vaccine = form.save(commit=False)
            user = request.user 
            account_obj = AccountModel.objects.get(user=user)
            if account_obj.account_type=='doctor':
                vaccine.doctor = account_obj
                vaccine.save()
                messages.success(request,'The vaccine is added successfully')
                return redirect('all_vaccines') 
            else :
                messages.error(request,'Only the doctor is authorised to add vaccines!')
    else:
        form = VaccineForm()

    return render(request, 'add_vaccine.html', {'form': form})


def edit_vaccine(request,id):
    vaccine = Vaccine.objects.get(pk=id)
    form = VaccineForm(instance=vaccine)
    if request.method=='POST':
        form = VaccineForm(request.POST,instance=vaccine)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    return render(request,'edit_vaccine.html',{'form':form})

def delete_vaccine(request,id):
    vaccine = Vaccine.objects.get(pk=id)
    vaccine.delete()
    return redirect('homepage')

def details(request,id):
    vaccine = Vaccine.objects.get(pk=id)
    obj = vaccine.doctor.account_type
    has_edit_access = False 

    if request.user.is_authenticated:
        doctor = False 
        account_type = obj
        
        if account_type == 'doctor':
            doctor=True 
            if vaccine.doctor==AccountModel.objects.get(user=request.user):
                has_edit_access= True 
    

    comments= Comment.objects.filter(Vaccine=vaccine) 
    if request.user.is_authenticated :
        has_taken = VaccineTaken.objects.filter(user=request.user, vaccine=vaccine).exists()
        return render(request,'details.html',{'has_edit_access':has_edit_access,'doctor':doctor,'db':vaccine,'has_taken':has_taken,'comment':comments})
    else :
        return render(request,'details.html',{'db':vaccine,'comment':comments})


def comment(request,id):
    form =CommentForm()
    if request.method=='POST':
        form =CommentForm(request.POST)
        if form.is_valid():
            vaccine = Vaccine.objects.get(pk=id)
            com = form.cleaned_data['comment']
            Comment.objects.create(user=request.user,Comment=com , Vaccine=vaccine)
            return redirect('vaccine_details',id=id)
    return render(request,'comment.html',{'form':form})



def all_vaccines(request):
    vaccines = Vaccine.objects.all()
    if request.user.is_authenticated:
        doctor = False 
        account_type = request.user.account.account_type
        
        if account_type == 'doctor':
            doctor=True 
            return render(request,'all_vaccines.html',{'db':vaccines,'doctor':doctor})
    return render(request,'all_vaccines.html',{'db':vaccines})
