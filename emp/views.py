from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , authenticate
from django.http import JsonResponse
from core.models import Profile
from django.db.models import Sum,Max,Min,Avg
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
#@login_required
def logout(request):
    #logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('emp:login')
#@login_required
def home(request):
    nm=request.session['username']
    un=User.objects.get(username=nm)
    type=un.type 
    sup=un.is_superuser
    empl=User.objects.filter(type="employer").count()
    user=User.objects.filter(type="users").count()
    return render(request,"home.html",{'type':type,'nm':nm,'sup':sup,'emp':empl,'user':user})
    #return render(request,"home.html",{'type':type,'nm':nm,'sup':sup})
#@login_required
def registration(request):
    form=Registrf()
    if request.method=="POST":
        form=Registrf(request.POST)
        if form.is_valid():
            form.save()
            typ=form.cleaned_data.get('type')
            un=form.cleaned_data.get('username')
            pas=form.cleaned_data.get('password1')
            em=form.cleaned_data.get('email')
            request.session['usrn']=un
            unn=request.session['usrn']
            messages.success(request,"registered successfully")
            subject = 'welcome to jku automated ems website'
            message = f'dear {un}, this is to inform you that you are registered as jku.. {typ}, your username is.. {un} your password is..{pas}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [em,]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,"core/add_profile.html",{'un':unn})
            #return redirect('emp:upadte')

    return render(request,"index.html",{'form':form})
#@login_required
def upadte(request):
    un=request.session['usrn']
    return render(request,"upadte.html",{'un':un})
#@login_required
def login(request):

    forma= AuthenticationForma()


    if request.method=='POST':
          forma = AuthenticationForma(data=request.POST)
          if forma.is_valid():
               username = forma.cleaned_data['username']
               request.session['username'] = username
               return redirect('emp:home')
          else:
              messages.warning(request,"please chack your entered information")

    return render(request,'login.html' ,{'forma':forma})
#@login_required
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
#@login_required
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
#@login_required
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
#@login_required
def eped(request,id):
    return render(request,"inde.html",{})
#@login_required
def dela(request,id):
    #en=Employe.objects.get(id=id)
    #en.delete()
    return redirect('emp:employ')
#@login_required
def empr(request):
    #en=Employe.objects.count()
    return render(request,"empr.html",{})
#@login_required
def atr(request):
    return render(request,'atr.html')
def search(request):
     #en=Employe.objects.filter()
     return render(request,'srch.html',{})
def update(request,id):
    return redirect('')
#@login_required
def salary(request):
    pr=Profile.objects.all()
    items =  Profile.objects.filter().aggregate(items=Sum("salary"))["items"]
    item =  Profile.objects.filter().aggregate(items=Max("salary"))["items"]
    min=  Profile.objects.filter().aggregate(items=Min("salary"))["items"]
    av =  Profile.objects.filter().aggregate(items=Avg("salary"))["items"]
    return render(request,"salary.html",{'profiles':pr,'sum':items,'max':item,'min':min,'av':av})
#@login_required
def upsalary(request,id):
    p=Profile.objects.get(id=id)
    if request.method=="POST":
      sla=request.POST.get('sal',False)
      p.salary=sla
      p.save()
      return redirect('emp:salary')
    items =  Profile.objects.filter().aggregate(items=Sum("salary"))["items"]
    item =  Profile.objects.all().aggregate(Max("salary"))
    #sun=Profile.objects.aggregate(Sum('salary'))["sun"]
    return render(request,"upsalary.html",{'p':p,'sum':items,'max':item})
#@login_required
def users(request):
    pro=Profile.objects.filter(type="users")
    
    
    
    return render(request,"user.html",{'profiles':pro})
#@login_required
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
#@login_required
def request(request):
    if  is_ajax(request=request):
    
        user=request.session['username']
        n=request.GET.get('txt')
        us=User.objects.get(username=user)
        nm=Request(username=us,msg=n,rsever=us)
        nm.save()
        rb=Request.objects.filter()
        return JsonResponse({'b':rb},status=200)
        #return redirect('emp:request')
    rb=Request.objects.filter()
    user=request.session['username']
    mn=Request.objects.filter(rsever=user) 
    #mn=User.objects.get(username=n)   
    return render(request,"request.html",{'b':rb,'n':mn})
#@login_required
def dlm(request,id):
    dg=Request.objects.get(id=id)
    dg.delete()
    return redirect('emp:request')
def profile(request):
    nm=request.session['username']
    us=User.objects.get(username=nm)
    id= us.id
    
    fn=Profile.objects.get(username=id)
    return render(request,"profile.html",{'fn':fn})