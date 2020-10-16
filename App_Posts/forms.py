from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from App_Posts.models import Posts, Like


class PostForm(forms.ModelForm):
    image = forms.ImageField(required=True, label="")
    caption = forms.CharField(required=True, label="",  widget=forms.TextInput(attrs={'placeholder':'Caption'}))
    class Meta:
        model = Posts
        fields = ["image", "caption", ]
