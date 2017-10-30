from rest_framework import serializers
from slider.models import Slides


class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slides
        fields = ('id', 'slide', 'title')