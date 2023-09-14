from urllib import request
from django.urls import path
from main.views import RefreshVideoAPIView, VideoListView, APITokenView

urlpatterns = [
    path('videos/refresh/', RefreshVideoAPIView, name="refresh_video_view"),
    path('api-token/', APITokenView, name="api_token_view"),
    path('videos/', VideoListView.as_view(), name='video-list'),
]