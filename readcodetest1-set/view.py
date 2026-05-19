# views.py

from django.shortcuts import render      #import render from library
from django.shortcuts import redirect    #import redirect from library

from django.contrib.auth import authenticate     
from django.contrib.auth import login               #import login logout autheticate feature to use in this class from libarry
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required   #use login_required feature to use in this class

from rest_framework import viewsets                         #from rest framework library import viewsets to make api class crud operations
from rest_framework.permissions import (                    #from rest framework library import feature to authenticate user and other feature
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)

from rest_framework.authentication import (        #improt token authentication so each user have token on each login session
    TokenAuthentication
)

from .models import Product                         #import product model   

from .forms import ProductForm                      #import productform form

from .serializers import ProductSerializer           #import prucctserializers

from .decorators import admin_only                   #import decorator admin only that i used above function to check if user is admin only he can run the function or test the function of block of code before checking user is admin



def home(request):                                  #function home to reder homepage

    products=Product.objects.all()          #get all products from db and store in product

    return render(
        request,                                #rennder the home page with all query products from db
        'home.html',
        {
            'products':products
        }
    )


@login_required                         #check either user requesting is logged in user
def create_product(request):                #define a function for craete product

    if request.method=="POST":              #check customer has post request that he send somethingh

        form=ProductForm(                   #get all the values that user post and put in form
            request.POST
        )

        if form.is_valid():    #check either data eneterd by user is valid no validation error or not

            product=form.save(      #if data is correct save the form but dont commit to db yet cause false
                commit=False
            )

            product.owner=request.user      #make the product user as same as logged in user

            product.save()                  #save product

            return redirect(            #redirect us to home
                'home'
            )

    else:     #ekse

        form=ProductForm()  #if not opst request hsoe the emmpty form


    return render(          
        request,                    #render the craete product page and show empty form
        'create.html',
        {
            'form':form
        }
    )


@admin_only                                     #for admins only not for other user
def dashboard(request):                         # define dashboard request

    total=Product.objects.count()               #query the total numbers of products 

    return render(
        request,                                #render the dashbaord page with total numbers of products
        'dashboard.html',
        {
            'total':total
        }
    )


def login_view(request):                                    #define function to validate the login method

    if request.method=="POST":                          #if request method is post

        username=request.POST.get(                  #get the username user give us
            'username'
        )

        password=request.POST.get(              #get the password user type
            'password'
        )

        user=authenticate(                  #authenticate and matches the username and password with what we hae in db
            request,
            username=username,
            password=password
        )

        if user:                            #if user

            login(
                request,                        #make user login 
                user
            )

            return redirect(
                'home'                          #and redirect him to home page
            )

    return render(
        request,
        'login.html'                    #if username not matched it will render him login page
    )


def logout_view(request):           #define function to logout method

    logout(request)                 #make usre logout if user press button

    return redirect(                #redirect the user to login page 
        'login'
    )



class ProductViewSet(            #(AS)       #edfine a class to get apirequest
    viewsets.ModelViewSet                   #defeine modelviewset
):

    queryset=Product.objects.all()      #queryset that all data is available for api operations

    serializer_class=(                      #serialize data 
        ProductSerializer
    )

    authentication_classes=[                #REQUIRE TOKEN AUTHETICATION ON EACH API REQUEST
        TokenAuthentication
    ]

    permission_classes=[
        IsAuthenticatedOrReadOnly               #MAKE LOGGED IN USER 
    ]