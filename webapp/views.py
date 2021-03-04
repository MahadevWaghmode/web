from django.shortcuts import render,redirect
from .models import movies
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,'index.html') 


def movie(request):
    return render(request, 'movie.html')

def searchm(request):
    if request.method=='POST':
        srch = request.POST['box']

        if srch:
            match = movies.objects.filter(Q(name__icontains=srch) 
                                        
                            )
            if match:
                return render(request,'result.html',{'result':match,'srch':srch})
 
    return render(request,'index.html')
def search(request):
    if request.method=='POST':
        srch = request.POST['box']

        if srch:
            match = movies.objects.filter(Q(name__icontains=srch) 
                                        
                            )
            if match:
                return render(request,'result.html',{'result':match,'srch':srch})
 
    return render(request,'index.html')

def game(request):
    return render(request, 'contruction.html')

def profile(request):
    return render(request, 'contruction.html')
    
def about(request):
    return render(request, 'contruction.html')
    
def contact(request):
    return render(request, 'contruction.html')
    
def software(request):
    return render(request, 'contruction.html')

