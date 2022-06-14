
from django import urls
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('adminauth.urls')),
    path('books/', include('books.urls'))

]

"""

default SuperUser(i.e. Admin) id: dishank, and password: 1234

Superuser can be created only using the command line.

they can log in using the UI.

Only superuser can add, update or delete the Book Records.

Non Super Users(e.g. Students) has right to just view the books and their details with available quantity


"""
