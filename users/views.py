from django.shortcuts import render, redirect
from .forms import SignupForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    return render(request,'home.html')

# register function will do both task of user registration and profile creation altogether
def register(request):

    registered = False   # flag to check if user is already registered

    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if signup_form.is_valid() and profile_form.is_valid():
            user = signup_form.save()
            user.save()

            profile = profile_form.save()
            profile.user = user
            profile.save()

            registered = True
        else:
            print(signup_form.errors, profile_form.errors)
    else:
        signup_form = SignupForm()
        profile_form = ProfileForm()

    context = {'registered':registered,'signup_form':signup_form,'profile_form':profile_form}
    return render(request,'registration.html',context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request,user)

            return redirect('home')
    else:
        return render(request, 'login.html')

@login_required(login_url= 'login')
def user_logout(request):
    logout(request)
    return redirect('home')