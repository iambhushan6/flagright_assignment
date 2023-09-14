from django.db import models

# Create your models here.


class Video(models.Model):
    '''
    Video table will store all data related to a fetched video.
    '''
    title = models.CharField(max_length=500)
    identifier = models.CharField(max_length=200, db_index=True, unique=True)
    description = models.TextField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    thumbnail_url = models.CharField(null=True, blank=True, max_length=500)


class ApiToken(models.Model):
    '''
    ApiTokens of respective domains will be saved in table with status of expiry
    '''
    token = models.CharField(max_length=200)
    is_expired = models.BooleanField(default=False)
    domain = models.CharField(max_length=200, default='youtube.com')

