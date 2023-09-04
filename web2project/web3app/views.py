from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,
                               password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"somthing is wrong try again")
            return redirect('login')

    return render(request,"login.html")
def web3app(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        lastn = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('web3')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"there is already a user with same email")
                return redirect('web3')
            else:
                user = User.objects.create_user(username= username,first_name=first_name,last_name=lastn, email=email,password=password)

                user.save();
                print("user created")
        else:
            messages.info(request,"password doesn't match")
            return redirect('web3')

        return redirect('/')
    return render(request,"web3app.html")
def logout(request):
    auth.logout(request)
    return redirect('/')