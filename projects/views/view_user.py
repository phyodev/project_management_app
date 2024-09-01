from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import (
    logout,
    views as auth_views
)
from ..forms.user_forms import UserRegisterForm


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your account has been created! You are now able to log in.')
                return redirect('login')
        else:
            form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

class login_user(auth_views.LoginView):
    template_name = 'users/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        return redirect('login')
    messages.success(request, "You have been logged out ....")
    return render(request, 'users/logout.html', {})