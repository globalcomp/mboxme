from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

def index(request):
   return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

@login_required
def home(request):
	return render(request, 'profile/home.html')