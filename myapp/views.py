from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model
from django.contrib import messages, auth
from .models import Features, displayusers
from .forms import AddProduct
from django.template import loader


# Create your views here.

def index(request):

    feature = Features.objects.all()
    return render(request, 'index.html', {'feature': feature})

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not same')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Login')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):

    auth.logout(request)
    return redirect( '/')

def term_of_service(request):

    return render(request, 'term_of_service.html')

def manage_admin(request):

    user = User.objects.all()
    template = loader.get_template('manage_admin.html')
    context = {'displayusers': user}
    return HttpResponse(template.render(context,request))

def manage_product(request):

    features = Features.objects.all()
    template = loader.get_template('manage_product.html')
    context = {'features': features,}
    return HttpResponse(template.render(context, request))


def add_product(request):

    return render(request, 'add_product.html')

def search_products(request):
    
    if request.method == 'POST':

        searched = request.POST['searched']
        products = Features.objects.filter(name__contains=searched)
        return render(request, 'manage_product', {'searched': searched, 'products': products})
    
    else:
        return render(request, 'manage_product', {})

