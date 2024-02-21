import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, VerificationForm, CardDet
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404, render
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .models import CustomerUser
from django.template.loader import render_to_string
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def login_user(request):
    #get post data
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    #authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Your Account have been logged in')
            return redirect('home')
        else:
            messages.success(request, 'Error Login in, Incorrect Username and Password')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "User logged out")
    return render(request, 'home.html')
def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have successfully create your account'))
            return redirect('welcome')
        else:
            messages.success(request, 'You failed to create your account')
            return redirect('register')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form' : form })
    return render(request, 'register.html', {'form' : form })

def welcome_user(request):
    return render(request, 'welcome.html')

def verify_account(request):
    if request.method == "POST":
        form = VerificationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully Verify your account')
            return redirect('home')
        else:
            messages.success(request, 'Failed to verify account')
            print(request)
            return redirect('welcome')
    return render(request, 'verify_acc.html', {'form' : VerificationForm})


def start_user(request):
    return render(request, 'starter.html')


def gift_card_page(request):
    return render(request, 'gift_card.html')

def gift_card_detail(request):
    if request.method == 'POST':
        card = CardDet(request.POST)
        if card.is_valid():
            card.save()
            messages.success(request, 'Sold, Payment in 5mins')
            return redirect('home')
        else:
            messages.success(request, 'Failed to verify Detail')
            print(request)
            return redirect('gift_card_detail')
    return render(request, 'gift_card_detail.html', {'card': CardDet})