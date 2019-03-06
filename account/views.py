from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def sign_up(request):
    if request.method == "POST":
        if request.POST.get('password') == request.POST.get('password-confirmation'):
            user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
            auth.login(request, user)
            return redirect('home')
    return render(request, 'sign_up.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'name or password is incorrect'})
    else:        
        return render(request, 'login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')