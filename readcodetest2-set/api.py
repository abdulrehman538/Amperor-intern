from rest_framework.views import APIView            #import apiview from the rest framework

from rest_framework.response import Response           #import reponse from the rest framework

from rest_framework.permissions import IsAuthenticated    #import isauthenticated from rest framework

from rest_framework import status           #import status from rest frmaework

from .models import Product                 #import product model from model file

from .serializers import ProductSerializer              #import Productserializer from serializer


class ProductListAPIView(APIView):                      #CLASS TO DEfine all the apiview operations

    permission_classes = [IsAuthenticated]              #it will indicate that user have permission or not


    def get(self, request):                     #define a function fot get api (to display )

        products = Product.objects.all()        #get the all product from product db and store in var

        serializer = ProductSerializer(         #validate the data and serialize it to json
            products,
            many=True                           #indicate that its a queryset or more then 1 data 
        )

        return Response(serializer.data)                #and returnthe serializes data


    def post(self, request):                        #define a function fort post request

        serializer = ProductSerializer(             #serialize the upcomming data and  validate 
            data=request.data
        )

        if serializer.is_valid():                   #if data is valid as per the model define inn ouyr model and validations

            serializer.save(owner=request.user)         #save the serialized data and make owner = the one who request or loggedin

            return Response(                            #return the serialize data with succesfull message 
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(                                #or else give error 
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )