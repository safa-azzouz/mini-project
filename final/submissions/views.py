from django.shortcuts import render

# Create your views here.
from .serializers import submissionsSerializer
from .models import submissions
from rest_framework import generics
from pygame import mixer

class submissionsList(generics.ListCreateAPIView):

    queryset = submissions.objects.all()

    serializer_class = submissionsSerializer


class submissionsDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = submissions.objects.all()
    serializer_class = submissionsSerializer






