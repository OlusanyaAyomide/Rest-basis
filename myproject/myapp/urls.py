from django.urls import path
from . import views
urlpatterns = [
    path('',views.watchList.as_view(),name='home'),
    path('platform',views.Platform.as_view(),name='platform'),
    path('<int:pk>',views.WatchListDetail.as_view(),name='detail'),
    path('platform/<int:pk>',views.PlatformDetail.as_view(),name='platform-detail'),
    path("reviews",views.ReviewList.as_view(),name="reviewlist"),
    path("review/<int:pk>",views.ReviewDetail.as_view(),name="review-detail"),
    path("review/<int:pk>/watch",views.WatchReview.as_view(),name="watchreview"),
    path("review/<int:pk>/review-create",views.ReviewCreate.as_view(),name="review-create")
]
