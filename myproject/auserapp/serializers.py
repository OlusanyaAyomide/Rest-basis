from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError


class UserSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model = User
        fields=["username","email","password","password2"]
        extra_kwargs={
            "password":{"write_only":True}
        }

    def validate(self,data):
        email=data["email"]
        username=data["username"]
        if data["password"] != data["password2"]:
            raise ValidationError("Password Do Not Match")

        if User.objects.filter(username=username).exists():
            raise ValidationError("Username Already In Use")
        
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email Already In Use")
        return data

    def save(self):
        new_user=User.objects.create(
            username=self.validated_data["username"],
            email=self.validated_data["email"],
            password=self.validated_data["password"])
        return new_user

    
