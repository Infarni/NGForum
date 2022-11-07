from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from os import remove
from os.path import isfile
from django.conf import settings


def index(request):
    if request.user.is_authenticated:
        avatar = request.user.avatar
        if request.method == 'POST':
            form = CustomUserAvatar(
                request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                if isfile(f'{settings.MEDIA_ROOT}/users_avatar/user_{request.user.username}/{request.user.avatar}'):
                    remove(f'{settings.MEDIA_ROOT}/users_avatar/user_{request.user.username}/{request.user.avatar}')
                form.save()
                return redirect('index')
            else:
                for msg in form.error_messages:
                    print(form.error_messages[msg])
        else:
            form = CustomUserAvatar()
            return render(request, 'users/index.html', {
                'form': form, 'avatar': avatar})
    else:
        return render(request, 'users/index.html')


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            login(request, form.save())
            return redirect("index")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(
                request,
                template_name="users/signup.html",
                context={"form": form}
            )
    else:
        form = CustomUserCreationForm()
        return render(
            request,
            template_name="users/signup.html",
            context={"form": form}
        )


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

    form = AuthenticationForm()
    return render(request, 'users/signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('index')
