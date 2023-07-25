from django.shortcuts import render
from .models import Login
from .forms import LoginForm
# Create your views here.

def login(request):
    if(request.method == "POST"):
       login_data= LoginForm(request.POST)
       if(login_data.is_valid):
           login_data.save()
    # username =request.POST.get("username")
    # password =request.POST.get("password")
    # data = Login(username=username,password=password)
    # data.save()
    return render(request,"pages/login.html",{"lf":LoginForm})