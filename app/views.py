from unicodedata import name
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.auth.models import User, auth
from app.models import PointsTable
# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,'home.html')

def login_user(request):
    if request.method=='POST':
        name = request.POST.get('name')

        user = authenticate(username=name,password=name)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return render(request,'login.html')


def home(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,'home.html')

def register(request):
    if request.method=='POST':
        name = request.POST['name']

        if User.objects.filter(username=name).exists():
            return render(request,'dup.html')
        else:
            user = User.objects.create_user(username
            =name,password=name)
            user.save()
    return render(request,'login.html')


def verify(request):
    points = 0
    if request.method=='POST':
        if request.POST['pic1'].lower()=='mercedes-benz':
            points+=1
        if request.POST['pic2'].lower()=='nike':
            points+=1
        if request.POST['pic3'].lower()=='shell':
            points+=1
        if request.POST['pic4'].lower()=='hmv':
            points+=1
        if request.POST['pic5'].lower()=='rothmans':
            points+=1
        if request.POST['pic6'].lower()=='pepsi':
            points+=1
        if request.POST['pic7'].lower()=='pontiac':
            points+=1
        if request.POST['pic8'].lower()=='kyocera':
            points+=1
        if request.POST['pic9'].lower()=='saab':
            points+=1
        if request.POST['pic10'].lower()=='pizza-hut':
            points+=1
        
    try:
        obj = PointsTable.objects.get(name=request.user.username)
        obj = obj.points
        obj = int(obj)
        print(type(obj))
    except:
        print("cant fetch !")
    

    if not PointsTable.objects.filter(name=request.user.username).exists():
        user  = PointsTable(name=request.user.username,points=points)
        user.save()
    else:
        if points > obj:
            PointsTable.objects.filter(name=request.user.username).update(points=points)
        
    print(points)
    
    return render(request,'home.html')

def leaderboard(request):
    objs = PointsTable.objects.all()
    context = {
        "object_list": objs
    }
    return  render(request,'leaderboard.html',context)