from django.db import models         #import model  

from django.contrib.auth.models import User     #import user from library that handle auth functions


class Category(models.Model):                   #define class of category

    title = models.CharField(max_length=100)        #title field with validation of 100 max lenght

    created_at = models.DateTimeField(auto_now_add=True)            #created at field with auto add to record at time creation


    def __str__(self):                                  #constructor that return the title of the category

        return self.title


class Product(models.Model):                            #define a class of products

    category = models.ForeignKey(                       #make category a parent of product so when the category delete it will delete the re;lated products
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    owner = models.ForeignKey(                          #make user  a parent of products so when user delete it will delete the related products
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=200)             #define a field for product name

    description = models.TextField()                    #DEFINE A FIELD FOR Product description 

    price = models.DecimalField(                        #defien a field price 
        max_digits=10,                                  #validation of max lenght of prive is 10 digit with  2 decimal
        decimal_places=2
    )

    stock = models.IntegerField(default=0)              #define a field sstock with default value 0

    is_available = models.BooleanField(default=True)    #define a checkbox field default true

    created_at = models.DateTimeField(auto_now_add=True)    #defien a field of created at that will add automatically to record when it created


    def __str__(self):                                  # #constructor that return the title of the products

        return self.name


class Order(models.Model):                              #define a class of products   

    customer = models.ForeignKey(                       #make customer a parent so when customer got deleted it will delete the related orders
        User,
        on_delete=models.CASCADE
    )

    products = models.ManyToManyField(Product)              #make a lookup relation that mean order nay contains multiple products

    total_price = models.DecimalField(                      #define a field of total price where max digit will be 1o with decimal of 2
        max_digits=10,
        decimal_places=2
    )

    is_paid = models.BooleanField(default=False)            #defiene a boolean checkbx that woll tell order payment done or not

    created_at = models.DateTimeField(auto_now_add=True)        #define a created a field that add automatically when the record created


    def calculate_total(self):                                  #function define to add total price

        total = 0                           #total varaible with value of 0

        for product in self.products.all():             #for loop wheere it will go through list of all prduct

            total += product.price                      #add the product price in total variable 

        return total                    #return total