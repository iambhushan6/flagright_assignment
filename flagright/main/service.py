import requests
from django.conf import settings
from datetime import datetime, timedelta
from main.models import Video, ApiToken


class YoutubeDataService:
    '''
    YoutubeDataService fetched video data from youtube api using api token and save it into the db.
    '''

    def fetch_videos() -> bool:

        api_token_instance = ApiToken.objects.filter(domain="youtube.com", is_expired=False).first()
        print(api_token_instance.token)

        current_datetime = datetime.now() - timedelta(minutes=10)   # to let google api update video data

        params = {
            "key" : api_token_instance.token if api_token_instance else settings.YOUTUBE_API_KEY,
            "part" : "snippet",
            "q" : "cricket",
            "maxResults" : 20,
            "type" : "video",
            "publishedAfter" : str(current_datetime.isoformat('T',timespec='seconds')) + 'Z'
        }

        # Youtbe video api call
        response = requests.get(url="https://www.googleapis.com/youtube/v3/search", params=params)

        # Mark expired token as expired.
        if response.status_code != 200:
            api_token_instance.is_expired = True
            api_token_instance.save(update_fields=['is_expired'])
            return False

        video_data = response.json()["items"]

        # Save video data in db
        video_instances_to_be_saved = []
        for data in video_data:
            video_instances_to_be_saved.append(
                Video(
                    title= data["snippet"]["title"],
                    description= data["snippet"]["description"],
                    published_at= data["snippet"]["publishedAt"],
                    identifier= data["id"]["videoId"],
                    thumbnail_url= data["snippet"]["thumbnails"]["default"]["url"]
                )
            )
        Video.objects.bulk_create(video_instances_to_be_saved, ignore_conflicts=True)
        return Video.objects.all().count()