from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        "name":"ahmed00",
        "age":"2011515"
    }
    return render(request=request,template_name="pages\index.html",context=data)

def about(request):
    pass