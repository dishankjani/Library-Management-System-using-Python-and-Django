from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Books
# Create your views here.

class UplaodBook(CreateView):

    model = Books
    template_name = 'upload_book.html'
    fields = '__all__'
    success_url = reverse_lazy('listbooks')

    

class ViewBooks(ListView):

    model = Books
    template_name = 'book_list.html'
    context_object_name = 'bookaccess'


class MyBookUpdate(UpdateView):
    model = Books
    fields = '__all__'
    success_url = reverse_lazy('listbooks')
    template_name = 'upload_book.html'    


class DeleteBook(DeleteView):
    model = Books
    success_url = reverse_lazy('listbooks')
    template_name = 'delete_book.html'    

