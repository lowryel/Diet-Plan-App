from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
from .forms import fill_formForm

# Create your views here.

def fill_form(request):
    if request.method=="POST":
        age = request.POST['age']
        weight = request.POST['weight']
        height = request.POST['height']
        weekly_budget = request.POST['weekly_budget']
        gender = request.POST['gender']
        lifestyle = request.POST['lifestyle']
        goals = request.POST['goals']
        foods = request.POST['foods']
        fill_form = fill_formModel.objects.create(
            age=age, weight=weight, height=height, weekly_budget=weekly_budget, gender=gender, lifestyle=lifestyle, goals=goals, foods=foods
    )
        messages.success(request, "Form Data submitted Successfully")
        return redirect('index')
    else:
        return render(request, 'fill_form.html')


def index(request):
    
    form_items, created= fill_formModel.objects.get_or_create(user=request.user)
    BMI =form_items.weight / (form_items.height*form_items.height)
    
    context= {
        'form_items':form_items,
        'bmi':BMI
    }
    return render(request, 'index.html', context)

def update_info(request):
    if request.user.is_authenticated:
        form_items= fill_formModel.objects.get(id=10)
        form = fill_formForm(request.POST or None, instance=form_items)
        if form.is_valid():
            form.save()
            return redirect('index')

    context={
        'form':form
    }
    return render(request, 'update_info.html', context)



def signup(request):
    if request.method =="POST":
        Username = request.POST['Username']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Password2 = request.POST['Password2']

        if Password == Password2:
            if User.objects.filter(email=Email).exists():
                messages.info(request, 'Email already Used')
                return redirect('signup')
            elif User.objects.filter(username=Username).exists():
                messages.info(request, 'Username already Used')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=Username, email=Email, password=Password
                )
                user.save()  
                messages.info(request, "Signup successful")
                return redirect('fill_form')
        else:
            messages.info(request, 'password not the same')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method =='POST':
        Username = request.POST['Username']
        Password = request.POST['Password']
        user = auth.authenticate(username = Username, password=Password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
