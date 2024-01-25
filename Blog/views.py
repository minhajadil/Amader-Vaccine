from django.shortcuts import render,redirect
from .forms import PostForm
from django.contrib import messages
from Account.models import AccountModel
from .models import Posts

# Create your views here.

def add_post(request):
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author= AccountModel.objects.get(user= request.user)
            post.save()
            messages.success(request,'The blog has been posted !')
            return redirect('all_blogs')
        

    form = PostForm()

    return render(request,'add_post.html',{'form' : form })


def post_details(request,id):
    post = Posts.objects.get(id=id)
    return render(request,'post_details.html',{'post':post})


def all_blogs(request):
    posts = Posts.objects.all()
    return render(request,'all_blogs.html',{'posts':posts})
