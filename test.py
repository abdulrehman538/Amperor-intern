from rest_framework.views import APIView    
from rest_framework.response import Response

class productapi(APIView):

    def get(self, request):
        data = {
                "message": "Hello API"

        }
        return Response(data)