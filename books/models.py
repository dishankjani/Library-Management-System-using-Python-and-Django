from turtle import title
from django.db import models

# Create your models here.

class Books(models.Model):

    title = models.CharField(max_length=500, null=True)
    Book_details = models.TextField(max_length=100, null=True)
    author_name = models.CharField(max_length=500, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title

    
