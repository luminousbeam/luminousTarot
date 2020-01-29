from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
from apps.tarot.models import *

def index(request):
    return redirect('/tarot')

def entry(request):
    return render(request, 'log_reg/index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    new_user = User.objects.create(first_name=request.POST['first-name'], last_name=request.POST['last-name'], email=request.POST['email'], password=request.POST['password'])
    request.session['name'] = new_user.first_name
    request.session['id'] = new_user.id
    return redirect('/tarot')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    logged_in_user = User.objects.filter(email=request.POST['email'])
    if len(logged_in_user) > 0:
        user = logged_in_user[0]
        print(user)
        if request.POST['password'] == user.password:
            print("pw is ok")
            request.session['name'] = user.first_name
            request.session['id'] = user.id
            return redirect("/tarot")
    return redirect("/")

def view_account(request, id):
    user = User.objects.get(id=id)
    context = {
        "user": user,
        # "three_card_readings": ThreeCardReading.objects.all(),
        "all_tarots": Tarot.objects.all()
    }
            
    return render(request, 'tarot/my-account.html', context)


def edit_account(request, id):
    context = {
        "user": User.objects.get(id=id),
    }
    return render(request, 'tarot/edit-account.html', context)

def update_account(request, id):
    errors = User.objects.account_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/myaccount/' + id)
    current_user = User.objects.get(id=id)
    current_user.first_name = request.POST['first-name']
    current_user.last_name = request.POST['last-name']
    current_user.email = request.POST['email']
    current_user.save()
    return redirect('/user_account/' + id)

def logout(request):
    request.session.flush()
    return redirect("/tarot")
