from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(requet):
    return render(requet,'index.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        message = request.POST.get('message')
        ins=Contact(name=name, email=email, password=password, message=message)
        ins.save()
        print('data has been written to the db')
    return render(request,'contact.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

