from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):

    return render(request,"authantication/index.html")
def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname =request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpass = request.POST['confirmpass']

        
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()

        messages.success(request,"your account has been created")

        return redirect('signin')

    return render(request,"authantication/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username , password=password)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"authantication/index.html" , {"fname": fname})
        else:
            messages.error(request,"add Credentials")
            return redirect('home')

    return render(request,"authantication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')