from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    

    peoples=[
        {'name':'umar','age':10},
        {'name':'tirmizi','age':78},
        {'name':'faizan','age':15},
        {'name':'zain','age':20},
        {'name':'fahad','age':15},
        {'name':'aahad','age':50}
    ]
    
    return render(request,'home/index.html',context={'peoples':peoples,'page':'learning'})


def second_page(request):
    return HttpResponse("second page")


def contact(request):
#    context={'page':'contact'}
   return render(request,'home/contact.html',context={'page':'contact'}) 

def about(request):
   context={'page':'about'}
   return render(request,'home/about.html',context) 