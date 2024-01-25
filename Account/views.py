from django.shortcuts import render,redirect
from .forms import DoctorRegistrationForm ,PatientRegistrationForm,datachange
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from .models import AccountModel
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
import uuid


def send_verification_email(user,token ,template):
        message = render_to_string(template, {
            'user' : user,
            'token' : token
            
        })
        send_email = EmailMultiAlternatives('Please Confirm your Email', '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()


class signup_user(CreateView):
    model = User
    template_name = 'signup.html'
    form_class= PatientRegistrationForm
    success_url= reverse_lazy('login')
    def form_valid(self, form):
        nid = form.cleaned_data['nid']
        if AccountModel.objects.filter(nid=nid).exists():
          
            messages.error(self.request, 'A user with this NID already exists.')
            return redirect('user_signup')  
        else:
            our_user = super().form_valid(form)
            obj = AccountModel.objects.create(user=self.object,account_type='patient',nid=nid,email_token=str(uuid.uuid4()))
            send_verification_email(self.object,obj.email_token,'verification_email.html')
            messages.success(self.request,'Please check your email for verification')
            
            return our_user
    

class signup_doctor(CreateView):
    model = User
    template_name = 'signup.html'
    form_class= DoctorRegistrationForm
    success_url= reverse_lazy('homepage')




    def form_valid(self, form):
        our_user = super().form_valid(form)
        obj= AccountModel.objects.create(user=self.object,account_type='doctor',email_token=str(uuid.uuid4()))
        send_verification_email(self.object,obj.email_token,'verification_email.html')
        messages.success(self.request,'Please check your email for verification')
        return our_user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signup_doctor'] = True
        return context




def verify(request,token):
    try :
        user_obj = AccountModel.objects.get(email_token=token)
        user_obj.is_activated=True
        user_obj.save() 
        messages.success(request,'Email verification successfull!')
        return redirect('login')
    except Exception as e:
        messages.error(request,'Invalid Token')
        return redirect('login')




class login_user(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('homepage')
    def form_valid(self, form):
        # return super().form_valid(form)
        user_data = form.cleaned_data['username']
        user_obj = User.objects.get(username =user_data)
        account_obj = AccountModel.objects.get(user=user_obj)
        if account_obj.is_activated:
            return super().form_valid(form)
        else :
            messages.error(self.request,'Please verify your email')
            return redirect('login')
    
    def form_invalid(self, form):
        messages.error(self.request,"Credentials doesn't match")
        return super().form_invalid(form)
    


@login_required(login_url='login')
def userlogout(request):
    logout(request)
    messages.warning(request,'Logged out Successfully')
    return redirect('homepage')


@login_required(login_url='login')
def profile(request):
    doctor=False
    user = request.user
    account = AccountModel.objects.get(user =user)
    
    if account.account_type=='doctor':
        doctor=True 



    return render(request,'profile.html',{'user':user,'doctor':doctor})



@login_required(login_url='login')
def passchange(request):
    if request.method=='POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else :
        form = PasswordChangeForm(user=request.user)
    return render(request,'changepassword.html',{'form':form})


@login_required(login_url='login')
def passchangewithoutprev(request):
    if request.method=='POST':
        form =SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else :
        form = SetPasswordForm(user=request.user)
    return render(request,'changepassword.html',{'form':form})


@method_decorator(login_required(login_url='login'),name='dispatch')
class changeuserdata(UpdateView):
    model = User
    form_class = datachange
    template_name = 'changeuserdata.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'
    

