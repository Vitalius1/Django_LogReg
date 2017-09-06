from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
print User

def index(request):
    return render(request, "login_app/index.html")

def register(request):
    results = User.objects.registerVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
    else:
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = request.POST['password'])
        messages.success(request, "User has been created. Please log in.")
    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    return redirect('/')


    print results
    print "^&%&^*&(**&(*)*)&(*&)(&(*^)*)*&)("
    return
# Create your views here.
