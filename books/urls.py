from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [

path('bookslist/', views.ViewBooks.as_view(), name='listbooks'),
path('uploadbook/', views.UplaodBook.as_view(), name='uploadbook'),
path('bookupdate/<int:pk>', views.MyBookUpdate.as_view(), name='updatebook'),
path('deletebook/<int:pk>', views.DeleteBook.as_view(), name='updatebook'),

]