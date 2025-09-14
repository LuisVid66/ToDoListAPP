from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm, RegistroForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('tareas')
                else:
                    return HttpResponse('El usuario no está activo')
            else:
                return HttpResponse('La información no es correcta')
    else:
        form = LoginForm()
    return render(request, 'appLogin/login.html', {'form': form})


def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # No asignamos email porque ya no existe en el formulario
            user.save()
            username = user.username
            messages.success(request, f'Usuario {username} creado')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'appLogin/registro.html', {'form': form})


def inicio(request):
    return render(request, 'appLogin/inicio.html')