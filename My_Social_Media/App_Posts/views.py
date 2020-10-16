from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse,reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.models import User
from App_login.models import UserProfile, Follow
from App_Posts.models import Posts, Like

@login_required
def home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts = Posts.objects.filter(author__in=following_list.values_list('following'))
    liked_post = Like.objects.filter(user=request.user)
    liked_post_list = liked_post.values_list('post', flat=True)
    print(liked_post_list)
    if request.method == 'GET':
        post_search = request.GET.get('post_search', '')
        result = User.objects.filter(username__icontains = post_search)
    diction={
         'title':'Home | Social Media',
         'post_search': post_search,
         'result':result,
         'posts':posts,
         'liked_post_list':liked_post_list
    }
    #return HttpResponse(posts.values())
    return render(request, 'App_Posts/home.html', context=diction)


@login_required
def liked(request, pk):
    post = Posts.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post, user=request.user)
    if not already_liked:
        liked_post = Like(post=post, user=request.user)
        liked_post.save()
    return HttpResponseRedirect(reverse('App_Posts:home'))

@login_required
def unliked(request, pk):
    post = Posts.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post, user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Posts:home'))
