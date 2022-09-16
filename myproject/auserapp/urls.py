from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserAV,LogoutAV

urlpatterns=[
    path("login",obtain_auth_token,name = "login"),
    path("register",CreateUserAV.as_view(),name="create-user"),
    path("logout",LogoutAV.as_view(),name="logout")
]