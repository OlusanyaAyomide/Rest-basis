from rest_framework import serializers
from .models import WatchLists,StreamPlatform,Review,Profile,Photos

class ReviewSerializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        # fields="__all__"
        exclude=("watchlist",)

class WatchListserializer(serializers.ModelSerializer):
    review=ReviewSerializer(read_only=True,many=True)
    review_avg=serializers.SerializerMethodField()
    class Meta:
        model=WatchLists
        # fields="__all__"
        exclude=("platform",)

    def get_review_avg(self,object):
        reviews=object.review.all()
        average=[]
        if reviews.count() == 0:
            return 'No Review'
        for rating in reviews:
            average.append(rating.rating)
        return round(sum(average)/len(average), 2)
  

class Platformserializer(serializers.ModelSerializer):
    watchlist=WatchListserializer(many=True,read_only=True)
    class Meta:
        model = StreamPlatform
        fields='__all__'

        
class ProfileSerializer(serializers.ModelSerializer):
    profile_user=serializers.StringRelatedField(read_only=True)   
    class Meta:
        model =Profile
        fields="__all__"

class PhotosSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
    class Meta:
        model = Photos
        fields=["title","image","path"]

    def get_path(self,object):
        obj = f"https://res.cloudinary.com/da3wqzkz3/image/upload/v1664193313/{object.image}"
        return(obj)

