from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings
from service.models import Service
from contact.models import contact
from detail.models import detail
from bedset.models import bedset
from chairs.models import chairset
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout



def homepage(request):
   Contact=contact.objects.all()
   ServiceData=Service.objects.all()
   if request.method=="GET":
        num1=request.GET.get('servicename')
        if num1!=None:
            ServiceData=Service.objects.filter(service_title__icontains=num1)
            
   data={
        
        'ServiceData' :ServiceData,
        'Contact' :Contact
    }
   if request.user.is_authenticated:
        return render(request,'first.html',data)
   else:
         return redirect("/register")
def sofas(request):
     ServiceData=Service.objects.all()
     if request.method=="GET":
        num1=request.GET.get('servicename')
        if num1!=None:
            ServiceData=Service.objects.filter(service_title__icontains=num1)
      
       
     data={
        
        'ServiceData' :ServiceData
    }
     return render(request,'sofa.html',data)
 
def bedsets(request):
    beds=bedset.objects.all()
    if request.method=="GET":
        num1=request.GET.get('servicename')
        if num1!=None:
            beds=bedset.objects.filter( bed_title__icontains=num1)
       
     
    stk={
        'beds' : beds,
        
    }
    return render(request,'bedset.html',stk)
def chairss(request):
    chair=chairset.objects.all()
    if request.method=="GET":
        num1=request.GET.get('servicename')
        if num1!=None:
            chair=chairset.objects.filter(chairs_title__icontains=num1)
     
    stl={
        'chair' : chair
    }
    return render(request,'chairs.html',stl)

def ContactUss(request):
  
   
    if request.method=="POST":
            email = request.POST.get('email')
            fn=contact(contact_email=email)
            fn.save()
            
       
    return render(request,'ContactUs.html')

def details(request,pk):
    ServiceData=Service.objects.get(pk=pk)
   

    
    return render(request,'detail.html',{'ServiceData':ServiceData})

def detail2(request,pk):
    beds=bedset.objects.get(pk=pk)
   

    
    return render(request,'detail2.html',{'beds':beds})
def detail3(request,pk):
    chair=chairset.objects.get(pk=pk)
   

    
    return render(request,'detail3.html',{'chair':chair})
    
def cart(request,pk):
     ServiceData=Service.objects.all()
     ServiceData=Service.objects.get(pk=pk)

     return render(request,'cart.html',{'ServiceData':ServiceData})  

def addtocart(request,product_id):
  
   

    return render(request,'addtcart.html')


def Aboutus(request):
  

     return render(request,'aboutUs.html')  



def signaction(request):
    if request.method=="POST":
        if request.POST.get('password1')==request.POST.get('password2'):
            try:
                saveuser=User.objects.create_user(request.POST.get("name"),email=request.POST.get("email"),password=request.POST.get("password1")) 
                saveuser.save()
                return render (request,'signup_page.html',{'form':UserCreationForm(),'info':'This user '+request.POST.get("name")+' is successfully'})
            except IntegrityError:
                return render (request,'signup_page.html',{'form':UserCreationForm(),'info':'This user '+request.POST.get("name")+' is already exist'})
        else:
            return render (request,'signup_page.html',{'form':UserCreationForm(),'error':'Password does not match'})
    else:
        return render(request,'signup_page.html')

def loginuser(request):
    if request.method=="POST":
        loginsuccess=authenticate(request,username=request.POST.get('name'),password=request.POST.get('password'))
        if loginsuccess is None:
            return render (request,'login_page.html',{'form':AuthenticationForm(),'error':'This name and password does not match'})
        else:
            login(request,loginsuccess)
            return redirect('home')
    else:
        return render (request,'login_page.html',{'form':AuthenticationForm()})


  
def savedata(request):
    
    return render(request,'signup_page.html')
    
def signout(request):
    logout(request)
    return redirect('/login/')


