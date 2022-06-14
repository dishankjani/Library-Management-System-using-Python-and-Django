from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy


# Create your views here.

def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')

class registerPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm   
    success_url = reverse_lazy('home')
    
    #to redirect user to another page if succesfully authenticated
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(registerPage, self).form_valid(form)

    #if user is successfully registered then they will redirected to the tasks page else they will be on the same page only
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(registerPage, self).get(*args, **kwargs)



class LoginPage(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')





