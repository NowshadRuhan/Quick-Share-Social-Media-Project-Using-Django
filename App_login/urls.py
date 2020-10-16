from django.urls import path, include
from App_login import views

app_name = 'App_login'

urlpatterns = [
    path('', views.sign_up, name='signup'),
    path('login/', views.signIn, name='signin'),
    path('edit-profile/', views.profile_edit, name='editProfile'),
    path('profile/', views.profile, name='profile'),
    path('user/<username>/', views.user, name='userOther'),
    path('follow/<username>/', views.follow_user, name='follow'),
    path('unfollow/<username>/', views.unfollow_user, name='unfollow'),
    path('logout/', views.logout_user, name='logoutUser'),

]
