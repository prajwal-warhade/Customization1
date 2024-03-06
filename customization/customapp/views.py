from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def about(request):
    HttpResponse("Hello")

def Custom(request):
    return render(request,'index.html')