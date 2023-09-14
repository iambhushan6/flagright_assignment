from celery import shared_task
from main.service import YoutubeDataService

@shared_task(bind=True)
def scheduled_task_fetch_youtube_video_data(self):
    data = YoutubeDataService.fetch_videos()
    return data