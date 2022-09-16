import re
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

class CreateUserAV(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            account=serializer.save()
            data={}

            token,created=Token.objects.get_or_create(user=account)
            print(token)
            data["token"]=token.key
            data["username"]=account.username
            data["email"]=account.email
            return Response(data)
        return Response(serializer.errors)

class LogoutAV(APIView):
    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)