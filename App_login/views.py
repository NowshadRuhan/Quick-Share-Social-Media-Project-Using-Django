from django.shortcuts import render, HttpResponseRedirect
from App_login.forms import CreateNewUser, UserLoginForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse,reverse_lazy
from App_login.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from App_Posts.forms import PostForm
from django.contrib.auth.models import User
from App_login.models import UserProfile, Follow



# Create your views here.
def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('App_login:signin'))

    diction = {
        'title':'Sign Up | Social Media',
        'form':form,
        'registered':registered
    }
    return render(request, 'App_login/signUp.html', context=diction)

def signIn(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Posts:home'))
    diction={
        'title':'Sign In | Social Media',
        'form':form
    }
    return render(request, 'App_login/login.html', context=diction)

@login_required
def profile_edit(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = UserProfileForm(instance=current_user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = UserProfileForm(instance=current_user)
            return HttpResponseRedirect(reverse('App_login:profile'))
    diction={
        'title':'Edit Profile | Social Media',
        'form':form
    }
    return render(request, 'App_login/profile.html', context=diction)


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_login:signin'))


@login_required
def profile(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('App_Posts:home'))
    diction={
        'title':'Profile | Social Media',
        'form':form
    }
    return render(request, 'App_login/user.html', context=diction)


@login_required
def user(request, username):
    user_other = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=user_other)
    if user_other == request.user:
        return  HttpResponseRedirect(reverse('App_login:profile'))
    diction={
        'title':' | Social Media',
        'user_other':user_other,
        'already_followed':already_followed

    }
    return render(request, 'App_login/other_user_profile.html', context=diction)

@login_required
def follow_user(request, username):
    following_user = User.objects.get(username = username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    if not already_followed:
        followed_user = Follow(follower=follower_user, following=following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('App_login:userOther', kwargs={'username':username}))


@login_required
def unfollow_user(request, username):
    following_user = User.objects.get(username = username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('App_login:userOther', kwargs={'username':username}))
