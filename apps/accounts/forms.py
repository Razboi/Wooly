from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=25, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password Confirmation'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2'
        ]

    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        # if the password and the password confirmation are not the same raise an error
        if password != password2:
            raise forms.ValidationError("Passwords must match")

        # if there is a user with that username raise an error
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("That username has already been registered")

        # if the email is already registered raise an error
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email address has already been registered")

        return super(UserRegisterForm, self).clean()


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=25, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    # if the user/password combination does not exists raise an error
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Incorrect username or password")

        return super(UserLoginForm, self).clean()

