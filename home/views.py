from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact,Webapp
from django.contrib import messages
from home.models import Contact
# Create your views here.

def index(request):
    # context ={
    #     "name":"Pravin"
    # }
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "webservices.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been send.')
    return render(request, "contact.html")

# def website(request):
#     return render(request, "index.html")

def webapp(request):
    if request.method == "POST":
        name = request.POST.get('name')
        days = request.POST.get('days')
        webapp = Webapp(name=name, days=days, date=datetime.today())
        webapp.save()
    return render(request, "webapp.html")
#

def desktopapp(request):
    return render(request,'desktopapp.html')
#fetch data from database

def fetch_data(request):
    if request.method == "POST":
        all_data = Contact.objects.all()
        dbname = list(all_data)
        param ={'name':dbname}
        print(param)
        print(dbname)
        return render(request,'index.html',param)
