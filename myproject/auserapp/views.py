import re
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response

class CreateUserAV(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)