from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import login 
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import  createUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only


def home(request):
    return render(request, 'home.html')



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           # Redirect to a success page.
           return redirect('booking')
        else:
           # Return an 'invalid login' error message.
           messages.success(request, ("There was an error logging in please try again"))
           return redirect('accounts/login_user')

    else:
        return render(request, 'login.html');
    
    


def register(request):
    form = createUserForm()

    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            
            
            messages.success(request, ("Registration Successful"))
            return redirect('login')

    else: 
        form = createUserForm()
        
    context = {'form': form}
    return render(request, 'register.html', context);

def forgot(request):
    
    context = {}
    return render(request, 'page-forgot-password.html', context)