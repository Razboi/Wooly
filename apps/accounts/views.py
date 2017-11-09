from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render, reverse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.contrib import messages

from .forms import UserLoginForm, UserRegisterForm
from .tokens import account_activation_token
User = get_user_model()


def register_view(request):
    form = UserRegisterForm(request.POST or None)

    # if the form is valid set the user object and save it
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.is_active = False
        user.email = form.cleaned_data.get('email')
        user.save()

        current_site = get_current_site(request)
        # get the template + data and create the email message
        message = render_to_string("accounts/activation_email.html", {
            "user": user,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user)
        })

        # set the email subject
        mail_subject = "Activa tu cuenta en Wooly"
        # set the email address
        to_email = form.cleaned_data.get("email")
        # get the message, subject and address and send the email
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

        context = {
            "message_to_user": '''Un mensaje de confirmación ha sido enviado a tu email, por favor
                                        comprueba también la bandeja de spam.'''
        }
        return render(request, "snippets/message_template.html", context)

    # if its a get request or the posted form is not valid render the form
    template_name = 'accounts/form.html'
    context = {
        'form': form,
        'title': 'Registrate'
    }

    return render(request, template_name, context)


def login_view(request):
    form = UserLoginForm(request.POST or None)
    # GET
    is_login = True
    context = {
        'form': form,
        'title': 'Iniciar Sesión',
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
            return redirect(next_url)
        else:
            return redirect('landing')

    # if its a get request or the posted form is not valid render the form
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('landing')


def activate(request, uidb64, token):
    template_name = "snippets/message_template.html"
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))  # get the uid from the activation token
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # if the link is valid activate the account and login the user, else return an error message
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)

        context = {
            "message_to_user": '''Tu cuenta ha sido activada, ahora puedes comprar en Wooly.''',
            "link_back": True,
        }
        return render(request, template_name, context)
    else:
        context = {
            "message_to_user": """El link de activación es invalido, es posible que ya se haya utilizado.
                       Por favor ponte en contacto con nosotros.""",
            "link_back": True,
        }
    return render(request, template_name, context)
