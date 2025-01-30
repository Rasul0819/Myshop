from django.shortcuts import render,get_object_or_404,redirect

from . import forms
from . import models

from django.contrib.auth import login,logout,authenticate

# Create your views here.
def homepage(request):
    products = models.Product.objects.all()

    return render(request,'shop/home.html',{'products':products})


def detail(request,id):

    detail = get_object_or_404(models.Product,id=id)
    reviews = models.Reviews.objects.all()
    return render(request,'shop/detail.html',{'detail':detail,
                                         'reviews':reviews})
def sign_in(request):
    if request.method=='POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form=forms.LoginForm()
    return render(request,'users/login.html',{'form':form})

def sign_up(request):
    if request.method=='POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = forms.RegistrationForm()
    print(form)
    return render(request,'users/registration.html',{'form':form})


def log_out(request):
    if request.method =='GET':
        logout(request)
        return redirect('home')