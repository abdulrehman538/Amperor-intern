from rest_framework.views import APIView
from rest_framework.response import Response    

#CRUD

class ProductCRUD(APIView):
    #read data
    def get(self, request):
        products = product.object.all()
        serializer = productserializer(products, many=True)  
        return Response(serializer.data)  

    #create data

    def post(request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data)
        return Response(serializer.errors)
    
    #edit data
    def edit(request, product_id):
        products = product.object.get(id = product_id)
        serializer = productserilaizer(product, data=response.data)
        if serializer.isvalid():
            serializer.save()
            return response(serailizer.data)
        return Response(serailizer.errors)
                        
                        
    #del data
    def delete(request, product_id):
        products = product.object.get(id = product_id)
        delete.product()
        return Response(
            {
                "product deleted sucessfully"
            }
        )