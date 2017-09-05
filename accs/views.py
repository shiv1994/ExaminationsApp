from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

# Create your views here.

@login_required(login_url="login/")
def home(request):
    return render(request,"accs/home.html",{'block_title':'Home'})