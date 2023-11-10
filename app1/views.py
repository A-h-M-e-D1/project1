from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        email = request.POST.get('email','')
        password =request.POST.get('password','')
        re_password =request.POST.get('re_password','')

        # check if two password and repeatpassword are equal or not
        if password == re_password:
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email is already in use')
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.erro(request,'Username is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request,'Registration successful. You can now log in.')
                return redirect('login')
        else:
            messages.error(request,'Passwords do not match')
            return redirect('register')
    else:
        return render(request,'register.html')
    

# login 
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # Validate that both username and password are provided
        if not username or not password:
            messages.error(request, 'Please provide both username and password.')
            return redirect('login')

        user = auth.authenticate(request, username=username, password=password)

        # Check if user exists and the provided credentials are valid
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('register')

    else:
        return render(request, 'login.html')
    

def home(request):
    return render(request,'home.html')