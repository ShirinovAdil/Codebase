from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditUserInfo
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index_page(request):
    return render(request, 'personal/home.html')


def register(request):
    # Registration form
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            msg = messages.success(request, 'Account created successfully')
            return render(request, 'accounts/profile.html', {'messages':msg})
        return render(request, 'accounts/register.html', {'form': form})
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/register.html', args)


def login_view(request):
    # Log user in
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():

                user = form.get_user()
                login(request, user)
                messages.info(request, "Welcome!")
                return redirect('accounts:login')

        else:
            form = AuthenticationForm()

        return render(request, 'accounts/login.html', {'form': form})
    else:
        messages.info(request, 'You are logged in')
        return render(request, 'accounts/profile.html')


def logout_view(request):
    # Logout user
    if request.user.is_authenticated:
        if request.method == "POST":
            logout(request)
            return redirect('personal:HomeForm')
    else:
        return redirect('personal:HomeForm')


def profile(request):
    # See profile info
    if request.user.is_authenticated:
        args = {'user': request.user}
        return render(request, 'accounts/profile.html', args)
    else:
        return redirect('accounts:login')


@login_required(redirect_field_name='accounts:login')
def edit_profile(request):
    # Edit profile info
    if request.method == "POST":
        form = EditUserInfo(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
        else:
            return redirect('accounts:profile')
    else:
        form = EditUserInfo(instance=request.user)

        args = {'form': form}

        return render(request, 'accounts/edit_profile.html', args)


@login_required(redirect_field_name='accounts:login')
def change_password(request):
    # Edit profile password
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:profile')
        else:
            return redirect('accounts:change_password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}

        return render(request, 'accounts/change_password.html', args)


