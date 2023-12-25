from django.contrib import admin
from django.urls import path, include
from .views import TextSpeechView

urlpatterns = [
 
    path('text_to_speech/', TextSpeechView.as_view(), name='text_to_speech'),
]
