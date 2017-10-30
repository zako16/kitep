from rest_framework import serializers
from slider.models import Slides


class SlideSerializer(serializers.Serializer):
    class Meta:
        model = Slides
    id = serializers.IntegerField()
    title = serializers.CharField()
    slide = serializers.SerializerMethodField('get_slide_url')

    def get_slide_url(self, obj):
        return obj.slide.url
