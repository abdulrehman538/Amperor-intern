from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product # Assuming models.py is in the same app directory
from .serializers import ProductSerializer # Assuming serializers.py is in the same app directory


class ProductAPIView(APIView):

    def get(self, request):
        # Fetch all product objects from the database
        products = Product.objects.all()
        # Serialize the queryset of products
        serializer = ProductSerializer(products, many=True)
        # Return the serialized data as a JSON response
        return Response(serializer.data)