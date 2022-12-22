from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , authenticate
from django.http import JsonResponse
from core.models import Profile
# Create your views here.
def home(request):
    
    return render(request,"home.html",{})
def registration(request):
    form=Registrf()
    if request.method=="POST":
        form=Registrf(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registered successfully")
            return redirect('emp:register')
    return render(request,"index.html",{'form':form})
def login(request):

    forma=AuthenticationForm()


    if request.method=='POST':
          forma =AuthenticationForm(data=request.POST)
          if forma.is_valid():
               username = forma.cleaned_data['username']
               request.session['username'] = username
               return redirect('emp:home')
          else:
              messages.warning(request,"please chack your entered information")

    Context={
          'forma':forma
    }
    return render(request,'login.html',Context)
def emp(request):
    #form=Emp()
    if request.method=="POST":
        pass
       # form=Emp(request.POST)
        
        #if form.is_valid():
            #form.save()
            #messages.success(request,"saved successfully")
            #username=form.cleaned_data.get("username")
            #fname=form.cleaned_data.get("fname")
            #lname=form.cleaned_data.get("lname")
            #return redirect('emp:home')
    return render(request,"emp.html",{})
def employ(request):
    if request.method=="POST":
        fn=request.POST.get('fnam',False)
        ln=request.POST.get('lnam',False)
        un=request.POST.get('usernam',False)
        gn=request.POST.get('gende',False)
        pn=request.POST.get('phon',False)
        em=request.POST.get('ema',False)
        sl=request.POST.get('salar',False)
        ex=request.POST.get('exp',False)
        gf=request.POST.get('gfro',False)
        gy=request.POST.get('gyea',False)
        rol=request.POST.get('rol',False)
        bim=request.FILES.get('bimag',False)
       # en=Employe(fname=fn,lname=ln,username=un,gender=gn,phone=pn,email=em,salary=sl,exp=ex,gfrom=gf,gyear=gy,role=rol,bimage=bim)
        #en.save()
        #return redirect('emp:employ')
   
    else:
       # en=Employe.objects.filter()
        return render(request,'empl.html',{})
def empd(request,id):
    if request.method=="POST":
        fn=request.POST.get('fname',False)
        ln=request.POST.get('lname',False)
        us=request.POST.get('username',False)
        gen=request.POST.get('gender',False)
        phon=request.POST.get('phone',False)
        em=request.POST.get('email',False)
        sal=request.POST.get('salary',False)
        ex=request.POST.get('exp',False)
        gfrom=request.POST.get('gfrom',False)
        gyea=request.POST.get('gyear',False)
        bimag=request.FILES.get('bimage',False)
        #en=Employe.objects.get(id=id)
        #en.fname=fn
        #en.lname=ln
        #en.username=us
       #en.gender=gen
        #en.phone=phon
        #en.email=em
        #en.salary=sal
        #en.exp=ex
        #en.gfrom=gfrom
        #en.gyear=gyea
        #en.bimage=bimag
        #en.save()
        #redirect('.')
        
        
    emd=Profile.objects.get(id=id)
    return render(request,"empdeta.html",{'ep':emd})
def eped(request,id):
    return render(request,"inde.html",{})
def dela(request,id):
    #en=Employe.objects.get(id=id)
    #en.delete()
    return redirect('emp:employ')
def empr(request):
    #en=Employe.objects.count()
    return render(request,"empr.html",{})
def atr(request):
    return render(request,'atr.html')
def search(request):
     #en=Employe.objects.filter()
     return render(request,'srch.html',{})
def update(request,id):
    return redirect('')