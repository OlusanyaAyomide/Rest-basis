from django.urls import path
from . import views
urlpatterns = [
    path('',views.WatchListGV.as_view(),name='home'),
    path('platform',views.PlatformGV.as_view(),name='platform'),
    path('<int:pk>',views.WatchListDetail.as_view(),name='detail'),
    path("platform/<int:pk>/watch",views.PlatformEntryGV.as_view(),name="detail"),
    path('platform/<int:pk>',views.PlatformDetail.as_view(),name='platform-detail'),
    path("reviews",views.ReviewList.as_view(),name="reviewlist"),
    path("review/<int:pk>",views.ReviewDetail.as_view(),name="review-detail"),
    path("stream/<int:pk>/review",views.WatchReview.as_view(),name="watchreview"),
    path("stream/<int:pk>/review-create",views.ReviewCreate.as_view(),name="review-create")
]
