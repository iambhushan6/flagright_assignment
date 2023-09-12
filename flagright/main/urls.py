from urllib import request
from django.urls import path
from main.views import test_api_view

urlpatterns = [
    path('test/', test_api_view, name="test_view"),
]