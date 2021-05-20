from django.http.response import HttpResponse
from django.shortcuts import render,redirect 
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
     return redirect("/login")
    return render(request, 'index.html')
    
def about(request):
     return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')    
def contact(request):

     if request.method == "POST":
         name = request.POST.get('name')
         email = request.POST.get('email')
         description = request.POST.get('description')
          
         contact = Contact(name=name,email=email,description=description, date=datetime.today())
         contact.save()
         messages.success(request, 'Message details has been updated.')
     
         
     return render(request, 'contact.html') 




def loginuser(request):
    
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        
        user = authenticate(username=username, password=password)   
        
        if user is not None:
            login(request, user)        
            return redirect("/afterlogin")

        else:
        
            return render(request, 'login.html')
        
    return render(request, 'login.html')    
                


def logoutuser(request):
    logout(request)
    return redirect("/login")    



  
def afterlogin(request):
     return render(request, 'afterlogin.html')