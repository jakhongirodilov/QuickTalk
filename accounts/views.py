from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.template import Context
from django.contrib.sessions.models import Session

from .models import CustomUser, Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm



def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


def profile_edit(request, pk):
    profile = Profile.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()

            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'registration/profile_edit.html', {'form': form})

