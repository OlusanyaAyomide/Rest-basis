from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class StreamPlatform(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    url=models.URLField(max_length=200)

    def __str__(self):
        return self.name

class WatchLists(models.Model):
    name=models.CharField(max_length=200)
    stotyline=models.CharField(max_length=2000,null=True)
    platform=models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="watchlist")
    created=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    review_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="review_user",null=True)
    watchlist=models.ForeignKey(WatchLists,on_delete=models.CASCADE,related_name="review")
    description=models.CharField(max_length=2000,null=True,blank=True)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.description:
            return f"{self.description} | {self.watchlist.name}"
        return  f"{self.rating}  | {self.watchlist.name}"

class Profile(models.Model):
    profile_user= models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_profile")
    profile_image=models.FileField(upload_to="xmedia",null=True)
    slug=models.SlugField(default="slug",null=True)


    def __str__(self):
        return f"{self.profile_user.username} Profile"
    
    def save(self,*args,**kwargs):
        self.slug=f"{self.profile_user.username} profile"
        super().save(*args,**kwargs)

class Photos(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField("image")
