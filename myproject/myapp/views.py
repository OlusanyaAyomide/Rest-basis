from platform import platform
from rest_framework.views import APIView
from rest_framework import mixins,generics
from rest_framework.response import Response
from .models import WatchLists,StreamPlatform,Review
from .serializers import Platformserializer, WatchListserializer,ReviewSerializer
from rest_framework.exceptions import ValidationError
from .permissions import ReviewEditPermission
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.


class WatchListGV(generics.ListAPIView):
    queryset=WatchLists.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=WatchListserializer

class WatchListDetail(APIView):
    def get(self,request,pk):        
        movie=WatchLists.objects.get(pk=pk)
        serializer=WatchListserializer(movie)
        return Response(serializer.data)
        
    def put(self,request,pk):
        movie=WatchLists.objects.get(id=pk)
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


class PlatformGV(APIView):
    def get(self,request):
        platform =StreamPlatform.objects.all()
        serializer=Platformserializer(platform,many=True)
        return Response({'platforms':serializer.data})


class ReviewList(generics.ListAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

class PlatformEntryGV(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=WatchListserializer
    lookup_field="pk"

    def get_queryset(self):
        pk=self.kwargs['pk']
        platform=StreamPlatform.objects.get(pk=pk)
        return WatchLists.objects.filter(platform=platform)

    def perform_create(self,serializer):
        pk=self.kwargs['pk']
        platform=StreamPlatform.objects.get(pk=pk)
        serializer.save(platform=platform)



class ReviewDetail(generics.RetrieveUpdateAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[ReviewEditPermission]
    lookup_field="pk"
 
    def perform_update(self, serializer):
        pk=self.kwargs["pk"]
        review=Review.objects.get(pk=pk)
        movie=review.watchlist
        serializer.save(watchlist=movie)

class WatchReview(generics.ListAPIView):
    serializer_class=ReviewSerializer

    def get_queryset(self):
        pk= self.kwargs['pk']
        watchlist=WatchLists.objects.get(pk=pk)
        return Review.objects.filter(watchlist=watchlist)

class ReviewCreate(generics.ListCreateAPIView):
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        pk=self.kwargs["pk"]
        movie=WatchLists.objects.get(pk=pk)
        return Review.objects.filter(watchlist=movie)

    def perform_create(self,serializer):
        pk=self.kwargs["pk"]
        movie=WatchLists.objects.get(pk=pk)
        review_user=self.request.user
        check=Review.objects.filter(watchlist=movie,review_user=review_user)
        if check.exists():
            raise ValidationError("You Already Made a review for This Movie")
        serializer.save(review_user=review_user,watchlist=movie)
   