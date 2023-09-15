# Flagright Assignment

## Introduction:

### Video explanation: ```https://screenapp.io/app/#/shared/0e4ca1fa-d6c9-4d22-b8bf-b3f337bf9ab8```

- As per the assignment instructions this repository covers all the backend work dockerizatoin, youtube data fetching, celery, beat scheduling, adding multiple key support, get api with 
   filters, sorting, search and pagination, a refresh videos api and a pause/resume video fetching functionality as well.

- There are two models created to save video and token data namely Video and ApiToken. 

- Assignment is made with django-rest-framework using sqlite as database with periodic tasks running on celery beat and redis.

- I have setup a celery beat running every 10 seconds, fetching youtube videos for the searcy query 'CRICKET'.

## API Documentation
1) Youtube videos listing with search, filter, order and pagination [GET]:
Endpoint: ```http://127.0.0.1:8000/api/videos/?search=dhoni&ordering=-published_at```

2) Refresh youtube fetch videos [GET]:
Endpoint: ```http://127.0.0.1:8000/api/videos/refresh``` 

3) Pause/Resume background video fetching [GET]:
Endpoint: ```http://127.0.0.1:8000/api/videos/pause/?fetch_videos=0/1``` 

4) Multiple Youtube Api token support [POST]:
Endpoint: ```http://127.0.0.1:8000/api/api-token/ payload: {"token": "dummy_token"}``` 

## Run this project with Docker:
```
 Build: $ sudo docker build -t myapp .
 Compose: $ sudo docker-compose up
``` 
## Run this project in Localhost:
### Open 4 terminals and paste below command in each and press enter, also dont forget to replace celery_broker_url with "redis://127.0.0.1:6379" in settings.py
```
 redis: $ redis-server
 django-server: $ python manage.py runserver
 celery: $ celery -A flagright.celery worker -l info
 celery beat: $ celery -A flagright beat -l info
``` 

Server will start at ``` http://127.0.0.1::8000/``` 

Thank You!
 


