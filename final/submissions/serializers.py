from rest_framework import serializers

from .models import submissions

class submissionsSerializer(serializers.ModelSerializer):

    class Meta:

        model = submissions
        fields = ('num','text','message')
