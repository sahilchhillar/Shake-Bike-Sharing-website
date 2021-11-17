from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from register.models import Balance

# Create your views here.

#Register Page
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # print(username, email, password, confirm_password)
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                return render(request, template_name='register/register2.html', context={'confirm': 'Username exists'})

            elif User.objects.filter(email=email).exists():
                return render(request, template_name='register/register2.html', context={'confirm': 'Email exists'})

            else:
                # print(request.POST)
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_balance = Balance(username=username)
                user_balance.save()
                # print('User created')
                return render(request, template_name='register/login2.html', context={})
        
        else:
            return render(request, template_name='register/register2.html', context={'confirm': 'password mismatch'})

        # if password == confirm_password:
        #     return render(request, template_name='register/login.html', context={'confirm': 'Registered'})
        # else:
        #     #return render(request, template_name='register/login.html', context={'confirm': 'Not Registered'})
        #     return render(request, template_name='register/register.html', context={'confirm': 'Password mismatch'})
    else:
        return render(request, template_name='register/register2.html', context={})




#Login Page
def login_user(request):
    # print("hello")
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/index')
        else:
            return render(request, template_name='register/login2.html', context={'confirm': 'Invalid credentials'})
    else:
        return render(request, template_name='register/login2.html', context={})