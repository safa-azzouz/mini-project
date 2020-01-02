from django.shortcuts import render

# Create your views here.
from .models import voice
from pygame import mixer
from .serializers import voiceSerializer
from rest_framework import generics

class voiceList(generics.ListCreateAPIView):

    queryset = voice.objects.all()

    serializer_class = voiceSerializer


class voiceDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = voice.objects.all()

    serializer_class = voiceSerializer

def voiceplay(request,msg):
  queryset = voice.objects.all()
  serializer_class = voiceSerializer
  print("hiii",queryset)
  mixer.init()
  if ("3"== msg[0]):
        mixer.music.load(voice.file(queryset[2]))
        return(request,mixer.music.play())
  if ("2" == msg[0]):
    mixer.music.load(voice.file(queryset[1]))
    return (request, mixer.music.play())
  if ("1" == msg[0]):
    mixer.music.load(voice.file(queryset[0]))
    return (request, mixer.music.play())
  if ("4" == msg[0]):
    mixer.music.load(voice.file(queryset[3]))
    return (request, mixer.music.play())
  if ("5" == msg[0]):
    mixer.music.load(voice.file(queryset[4]))
    return (request, mixer.music.play())
  if ("6" == msg[0]):
    mixer.music.load(voice.file(queryset[5]))
    return (request, mixer.music.play())
