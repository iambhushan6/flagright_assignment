
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Video, ApiToken
from main.serializers import VideoSerializer
from rest_framework import generics, filters
from main.pagination import FlagrightPagination
from main.service import YoutubeDataService
from django_celery_beat.models import PeriodicTask, PeriodicTasks

# Create your views here.


@api_view(["GET"])
def RefreshVideoAPIView(request):

    if request.method == "GET":
        # YoutubeDataService.fetch_videos()
        return Response({"data": Video.objects.all().count()})
    
    return Response({"error": "Invalid request method."})


@api_view(["GET"])
def PauseVideoFetchingAPIView(request):

    if request.method == "GET":
        fetch_videos = request.query_params.get("fetch_videos")

        if not fetch_videos or fetch_videos not in ['0','1']:
            return Response({"error": "Please choose between 1/0 as command to fetch_videos"}, status=400)
        # Change enablement of beat task.        
        task = PeriodicTask.objects.filter(name='fetch-youtube-video-data').first()
        if fetch_videos == '1':
            task.enabled=True
        elif fetch_videos == '0':
            task.enabled=False
        task.save()
        PeriodicTasks.update_changed()  # let the beat reload periodic task from database

        return Response({"data": f"Fetching of videos has been changed to {task.enabled}"})
    
    return Response({"error": "Invalid request method."})


@api_view(["POST"])
def APITokenView(request):

    # Support for multiple keys for fetching videos
    if request.method == "POST":
        data = request.data

        if not data.get("token"):
            return Response({"error": "Please provide a valid token"}, status=400)
        
        # Skipping encryption of api token as this is a project
        ApiToken.objects.get_or_create(token=data["token"])
        return Response({"data": "Token saved successfully"}, status=200)
    
    return Response({"error": "Invalid request method."}, status=400)
    

class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all().order_by("-published_at")
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']    # Optimised search filter
    pagination_class = FlagrightPagination
    ordering_fields = ('published_at', 'title')
    

