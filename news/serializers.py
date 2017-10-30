from rest_framework import serializers
from news.models import News


class NewsSerializers(serializers.Serializer):
    class Meta:
        model = News
    id = serializers.IntegerField()
    title = serializers.CharField()
    image = serializers.SerializerMethodField('get_image_url')
    created_at = serializers.DateTimeField()

    def get_image_url(self, obj):
        return obj.image.url


class NewsDetailSerializers(serializers.Serializer):
    class Meta:
        model = News
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField(max_length=None)
    image = serializers.SerializerMethodField('get_image_url')
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def get_image_url(self, obj):
        return obj.image.url
