from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from App_login.models import UserProfile


class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Email*'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Username*'}))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder':'Password*'}))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder':'Password confirmation*'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Username*'}))
    password = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder':'Password*'}))
    class Meta:
        model = User
        fields = ('username', 'password')

class UserProfileForm(forms.ModelForm):
    dob = forms.DateField(label="Date of Birth", widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = UserProfile
        exclude= ('user',)
