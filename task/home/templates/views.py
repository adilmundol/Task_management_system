from django.shortcuts import render,redirect
from .models import Task,Status
from .forms import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .serializers import TaskSerializer,TaskSerializer2
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def homefn(request):
    x=Task.objects.all()
    y=Status.objects.all()
    return render(request, 'home.html',{'post':x,'cat':y})
def homefn1(request):
    x=Task.objects.all()
    y=Status.objects.all()
    return render(request, 'home1.html',{'post':x,'cat':y})
def catfn(request,c_id):
    x=Task.objects.filter(status=c_id)
    y=Status.objects.all()
    return render(request,'status.html',{'post':x,'cat':y})
@login_required(login_url='/login') 
def addfn(request):
   
    if request .method=='POST':
        y=Status.objects.all()
        f=Taskform(request.POST,request.FILES)
        if f.is_valid():
            f.save()
            return redirect('/')
        else:
            return render(request,'add.html',{'form':f,'cat':y})
    else:
        y=Status.objects.all()
        return render(request,'add.html',{'form':Taskform(),'cat':y})
    
def viewfn(request,s_id):
    z=Task.objects.get(id=s_id)
    y=Status.objects.all()
    return render(request, 'viewpage.html',{'i':z,'cat':y})
@login_required(login_url='/login') 
def deleteproduct(request, p_id):
    if request.method == 'POST':
        p =Task.objects.get(id=p_id)
        p.delete()
        return redirect('/') 
    else:
        p =Task.objects.get(id=p_id)
        return render(request,'delete.html',{'pro':p})
@login_required(login_url='/login')    
def editproduct(request, p_id):
    p = Task.objects.get(id=p_id)
    if request.method == 'POST':
        f = Taskform2(request.POST, request.FILES, instance=p)
        if f.is_valid():
            f.save()
            return redirect('/') 
        else:
            x=Task.objects.all()
            return render(request, 'add.html', {'form': f, 'post': x})
    else:
        f = Taskform2(instance=p)
        x=Task.objects.all()
        return render(request, 'add.html', {'form': f, 'post': x})
    
def loginfn(request):
    if request.method=='POST':
        a=request.POST['user']
        e=request.POST['pass']
        u=auth.authenticate(username=a,password=e)
        if u:
            auth.login(request,u)
            return redirect('/')
        else:
            messages.error(request,'invalid username or password')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    
def regfn(request):
    if request.method == 'POST':
        a = request.POST['user']
        b = request.POST['fname']
        c = request.POST['lname']
        d = request.POST['mail']
        e = request.POST['pass']
        f = request.POST['cpass']
        
        if e == f:
            if User.objects.filter(username=a).exists():
                messages.error(request, 'username already exist')
                return render(request, 'register.html')
            elif User.objects.filter(email=d).exists():
                messages.error(request, 'email already exists')
                return render(request, 'register.html')
            else:
                User.objects.create_user(username=a, first_name=b, last_name=c, email=d, password=e)
                return redirect('/login')  
        else:
            messages.error(request, 'incorrect pass')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')
def logoutfn(request):
    auth.logout(request)
    return render(request,'login.html')



@api_view(['GET'])
def taskapifn(request):
        c=Task.objects.all()
        s = TaskSerializer(c, many=True)
   
        return Response(s.data)

@api_view(['GET'])
def viewtaskapifn(request,t_id):
        c=Task.objects.get(id=t_id)
        s = TaskSerializer(c, many=False)
   
        return Response(s.data)

@csrf_exempt
@api_view(['POST'])
def addtaskapifn (request):
        
        s = TaskSerializer(data=request.data)
        if s.is_valid():
             s.save()
             return Response(s.data)
        
@csrf_exempt
@api_view(['PUT'])
def updatetaskapifn (request,t_id):
        p=Task.objects.get(id=t_id)
        s = TaskSerializer2(data=request.data,instance=p)
        if s.is_valid():
             s.save()
             return Response(s.data)
        
@csrf_exempt
@api_view(['DELETE'])
def deletetaskapifn (request,t_id):
        p=Task.objects.get(id=t_id)
        p.delete()
        return Response("Done") 



def homefn2(request):
   
    return render(request, 'home2.html')


def viewfn2(request,s_id):
   
    return render(request, 'viewpage2.html',{'id':s_id})


def addfn2(request):
   
        return render(request,'add2.html')
    

def deleteproduct2(request, p_id):
  
        return render(request,'delete2.html',{'id':p_id})


     
def editproduct2(request, p_id):
   
    return render(request, 'edit.html',{'id':p_id})
    