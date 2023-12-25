from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pyttsx3

# Create your views here.
class TextSpeechView(APIView):
    def post(self,request,*args,**kwargs):
        text=request.data.get('text','')


        engiene=pyttsx3.init()
        engiene.say(text=request.data.get('text',''))
        engiene.setProperty('rate',125)
        engiene.setProperty('volume',1.0)
        engiene.setProperty('voice',engiene.getProperty('voices')[1].id)
        
        engiene.runAndWait()
        return Response({'detail':'text to speech successfully'},status=status.HTTP_201_CREATED)