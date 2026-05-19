# urls.py

from django.urls import path       #FROM DJANGO LIBRARY import path feature
from django.urls import include         #from django library import include feature

from rest_framework.routers import (            #from rest frmaework import deault router feature
    DefaultRouter
)

from .views import home                        
from .views import create_product
from .views import login_view                        #from views import all those functions we define 
from .views import logout_view
from .views import dashboard

from .views import ProductViewSet                  


router = DefaultRouter()                        #define all kind of  route for every api crud operation for product models

router.register(
    'products',                                     
    ProductViewSet
)


urlpatterns = [                                     #manually define url for template

    path(
        '',
        home,                       #for home
        name='home'
    ),

    path(
        'create/',
        create_product,                 #for create product
        name='create'
    ),

    path(
        'login/',
        login_view,                     #for login
        name='login'
    ),

    path(
        'logout/',
        logout_view,                    #for logout
        name='logout'
    ),

    path(
        'dashboard/',
        dashboard,
        name='dashboard'                #for dashboard
    ),

    path(
        'api/',
        include(                             #include the router url path for api calls
            router.urls
        )
    )

]