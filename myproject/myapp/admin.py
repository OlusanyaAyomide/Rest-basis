from django.contrib import admin
from .models import WatchLists,StreamPlatform,Review,Profile
# Register your models here.
admin.site.register(WatchLists)
admin.site.register(StreamPlatform)
admin.site.register(Review)
admin.site.register(Profile)