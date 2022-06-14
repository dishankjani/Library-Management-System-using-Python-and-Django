from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.home, name='home'),
    path('register/', views.registerPage.as_view(), name='register'),
    path('login/', views.LoginPage.as_view(), name='loginpage'),
    path('logout/', LogoutView.as_view(next_page = 'loginpage'), name='logout'),
]
