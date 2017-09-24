from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *

def index(request):
    return render(request, 'login_register/index.html')

def success(request):
    context = {
        'user' : Users.objects.get(id=request.session['id']).first_name
    }
    return render(request, 'login_register/success.html', context)

def create(request):
    errors = Users.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = Users.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashed_pw)
        request.session['id'] = user.id
        request.session['status'] = 'reg'
    return redirect('/success')
    
def login(request):
    errors = Users.objects.loginValidator(request.POST)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        request.session['id'] = Users.objects.get(email=request.POST['email']).id
        request.session['status'] = 'logged in'
    return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')

    
    