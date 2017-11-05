from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render, reverse
from django.http import HttpResponseRedirect, HttpResponse

from .forms import UserLoginForm, UserRegisterForm


def register_view(request):
    form = UserRegisterForm(request.POST or None)

    # if the form is valid set the user object and save it
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.is_active = True
        user.email = form.cleaned_data.get('email')
        user.save()
        login(request, user)
        return redirect('landing')

    # if its a get request or the posted form is not valid render the form
    template_name = 'accounts/form.html'
    context = {
        'form': form,
        'title': 'Sign Up'
    }

    return render(request, template_name, context)


def login_view(request):
    form = UserLoginForm(request.POST or None)
    # GET
    is_login = True
    context = {
        'form': form,
        'title': 'Login',
        'login': is_login
    }
    template_name = 'accounts/form.html'

    # POST
    # if the form is valid the user will be authenticated and logged
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        next_url = request.GET.get('next')
        # if there is a next url redirect to that url
        if next_url:
            return HttpResponseRedirect(next_url)
        else:
            return redirect('landing')

    # if its a get request or the posted form is not valid render the form
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('landing')
