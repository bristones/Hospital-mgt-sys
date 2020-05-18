from django.shortcuts import render, redirect
import templates
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages,auth
from django.contrib.auth import update_session_auth_hash
from .models import CustomUser

# # Create your views here.
def UserLogin(request):
    print('user login request')
    if request.method == "POST":
        form = request.POST
        username = request.POST.get('username')
        password  = request.POST.get('password')
        user = authenticate(username=username,password=password)
     
        if user is not None:
            login(request, user)
            print('logged in')
            return redirect('staff:profile')
        
        else:
            messages.info(request,'Invalid username or Password')
            return redirect('staff:login')
            
    return render(request,"Staff/login.html")


def Register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
    context = {'form':form}
    return render(request,"Staff/register.html",context)
    

def staffProfile(request):
    
    return render(request, 'Staff/dashboard.html')


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, "Staff/login.html")

# def password_change(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(user=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#     else:
#         ...
