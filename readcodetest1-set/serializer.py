# serializers.py

from rest_framework import serializers   #from rest_framework library import serializer
from .models import Product, Order          #from models files import order and product model
from django.contrib.auth.models import User   #from django.contrib.auth.models import user to use logout login authenticate features


class ProductSerializer(    #create a class with modelserialization that do tell modelserialzer will be used
    serializers.ModelSerializer
):

    class Meta:             #craete class and serialize all fields of products models
        model = Product
        fields = '__all__'


class OrderSerializer(          ##create a class with modelserialization that do tell modelserialzer will be used
    serializers.ModelSerializer 
):

    class Meta:         #craete class and serialize all fields of order  models
        model = Order
        fields = '__all__'


class UserSerializer(                       ##create a class with modelserialization that do tell modelserialzer will be used
    serializers.ModelSerializer
):

    class Meta:                     #craete class and serialize defiined fields of user  models
        model = User
        fields = ['id','username','email']