from django.urls import path, include
from App_Posts import views

app_name = 'App_Posts'

urlpatterns = [
    path('', views.home, name='home'),
    path('like/<pk>/', views.liked, name='like'),
    path('unlike/<pk>/', views.unliked, name='unlike'),

]
