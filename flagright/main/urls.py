from urllib import request
from django.urls import path
from main.views import RefreshVideoAPIView, VideoListView, APITokenView, PauseVideoFetchingAPIView

urlpatterns = [
    path('api-token/', APITokenView, name="api_token_view"),
    path('videos/', VideoListView.as_view(), name='video-list'),
    path('videos/refresh/', RefreshVideoAPIView, name="refresh_video_view"),
    path('videos/pause/', PauseVideoFetchingAPIView, name="pause_start_video_fetch_view"),
]