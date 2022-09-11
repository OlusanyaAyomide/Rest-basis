from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import mixins,generics
from rest_framework.response import Response
from .models import WatchList,StreamPlatform,Review
from .serializers import Platformserializer, WatchListserializer,ReviewSerializer
# Create your views here.


class watchList(APIView):
    def get(self,request):
        movies = WatchList.objects.all()
        serializer=WatchListserializer(movies,many=True)
        return Response({"all":serializer.data})

    def post(self,request):
        serializer=WatchListserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        else:
            return serializer.errors



class WatchListDetail(APIView):
    def get(self,request,pk):        
        movie=WatchList.objects.get(id=pk)
        serializer=WatchListserializer(movie)
        return Response(serializer.data)
        
    def put(self,request,pk):
        movie=WatchList.objects.get(id=pk)
        serializer=WatchListserializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class PlatformDetail(APIView):
    def get(self,request,pk):        
        platform=StreamPlatform.objects.get(id=pk)
        serializer=Platformserializer(platform)
        return Response(serializer.data)
        
    def put(self,request,pk):
        platform=StreamPlatform.objects.get(id=pk)
        serializer=Platformserializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Platform(APIView):
    def get(self,request):
        platform =StreamPlatform.objects.all()
        serializer=Platformserializer(platform,many=True)
        return Response({'platforms':serializer.data})


class ReviewList(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class ReviewDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    lookup_field="id"

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
      return self.update(request,*args,**kwargs)


