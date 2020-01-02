from rest_framework import serializers

from .models import voice

class voiceSerializer(serializers.ModelSerializer):

    class Meta:

        model = voice
        fields = ('num','text','message')
