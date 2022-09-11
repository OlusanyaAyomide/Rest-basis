from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class StreamPlatform(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    url=models.URLField(max_length=200)

class WatchList(models.Model):
    name=models.CharField(max_length=200)
    stotyline=models.CharField(max_length=2000,null=True)
    platform=models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="watchlist")
    created=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    watchlist=models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name="review")
    description=models.CharField(max_length=2000,null=True,blank=True)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.description:
            return f"{self.description} | {self.watchlist.name}"
        return  f"{self.rating}  | {self.watchlist.name}"