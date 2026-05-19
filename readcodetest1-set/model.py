# models.py

from django.db import models                            #import models from django.db library
from django.contrib.auth.models import User             #import user from library that we use to autheticate functionality


class Category(models.Model):                                           #create a class of category to define the fields for models
    title = models.CharField(max_length=100)                                #title fields that we put limit of lenghth 100

    def __str__(self):                                                  #create a contstructor that automatically call when object craeted of that class
        return self.title                                                   #return the title automatically


class Product(models.Model):                                                  #another class for product model
    name = models.CharField(max_length=100)                                         #defines fields with validations
    description = models.TextField()                                                  #//
    price = models.DecimalField(max_digits=8, decimal_places=2)                                                  #//
    quantity = models.IntegerField()                                                  #//
    category = models.ForeignKey(                                                   #(as)it make category a parent and product a child that
        Category,                                                                   #defiine a category has many product
        on_delete=models.CASCADE                                                    #ON.DELETE MEANT IF category delete all related product will delete too
    )

    owner = models.ForeignKey(                                                  #(as)  it make owner parent and child product
        User,                                                                    #user has many products   
        on_delete=models.CASCADE                                                 #ON.DELETE MEANT IF user delete all related product will delete too
    )

    def __str__(self):                                                  #create contrsutor for this product model it will return name of product everytime it call
        return self.name