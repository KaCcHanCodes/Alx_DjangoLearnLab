from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login

def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog/login')  
    
    form = CustomUserForm()
    context = {'form': form}
    return render(request, 'blog/register.html', context)

def customlogin(request): 
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.authenticate(
                                    username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('blog/base')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'blog/login.html', context)

@login_required
def customlogout(request):
    logout(request)
    return redirect('blog/base')

def home(request):
    return render(request, 'blog/base.html')

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

@login_required
def posts(request):
    return render(request, 'blog/profile.html')