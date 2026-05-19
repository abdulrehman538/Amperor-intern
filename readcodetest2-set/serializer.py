from rest_framework import serializers      #import serializer from rest framework library

from .models import Product, Category           #import porduct category from model file


class CategorySerializer(serializers.ModelSerializer):              #class cto define category serializer


    class Meta:                                             #class to define field to serialize

        model = Category                                    #defeine model here

        fields = '__all__'                                      #all fields of that model


class ProductSerializer(serializers.ModelSerializer):           #class to define product serializer

    category = CategorySerializer(read_only=True)               #as they have relationship we have to tell category serialization is from the categoryserailizer class read only

    owner = serializers.StringRelatedField()                    #not sure


    class Meta:                                             #class to define sserialize fields

        model = Product             #define which model here which model

        fields = [                          #define which fields to serialzie listed under the list
            'id',
            'name',
            'description',
            'price',
            'stock',
            'category',
            'owner'
        ]


    def validate_price(self, value):                #function to validate price with parameter of value

        if value <= 0:                                          #condition if price is in negative
            raise serializers.ValidationError(              #raise serialier validatiopm error 
                "Price must be greater than zero"       #error nesssage
            )

        return value                    #return value