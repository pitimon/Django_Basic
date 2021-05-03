from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.models import User,auth
from django.contrib import messages

#from django.http import HttpResponse

# Create your views here.
def hello(request):
    #Query data from model
    data=Post.objects.all()
    return render(request,'index.html',{'posts':data})

def page1(request):
    return render(request,'page1.html')

def createForm(request):
    return render(request,'form.html')

def loginForm(request):
    return render(request,'login.html')

def login(request):
    username=request.POST['username']
    password=request.POST['password']
    #login
    user=auth.authenticate(username=username,password=password)

    if user is not None :
        auth.login(request, user)
        return redirect('/data')
    else :
        messages.info(request, 'Unknow ...')
        return redirect('/loginForm')


def addUser(request):
    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['repassword']

    if password==repassword :
        if User.objects.filter(username=username).exists():
            messages.info(request,'Exis username')
            return redirect('/createForm')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Exis Email')
            return redirect('/createForm')
        else :
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname
                )
            user.save()
            return redirect('/data')
    else :
        messages.info(request,'Password not same')
        return redirect('/createForm')

def logout(request):
    auth.logout(request)
    return redirect('/')

#    return HttpResponse('Hello world')