from .serializers import*
from rest_framework import serializers
class TextSerializers(serializers.Serializer):
    text=serializers.CharField(max_length=1000)