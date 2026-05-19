from django.shortcuts import render                     #from django library import render 

from .models import Product                             #from model library import product


def dashboard_view(request):                            #define a function to for dashboard

    products = Product.objects.all()                    #query all the data of product and store in products var

    expensive_products = Product.objects.filter(price__gte=1000)      #query out all the porducts that have higer price store in expensive_products 

    total_products = products.count()                                   #count the total numbers of products you have 


    context = {                                                         #show or transfer the followinhg data view to template
        'products': products,
        'expensive_products': expensive_products,
        'total_products': total_products
    }

    return render(                  #return the dashboard page with the data 
        request,
        'dashboard.html',
        context
    )