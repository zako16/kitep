from rest_framework import serializers
from partners.models import Partners
from transliterate import translit, get_available_language_codes


class PartnersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ('id', 'title', 'description', 'image', 'created_at', 'slug', 'updated_at')


class PartnersDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ('id', 'title', 'description', 'image', 'created_at', 'slug', 'updated_at')


class PartnersModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ('title', 'description', 'image')
        read_only_fields = ('created_at', 'slug', 'updated_at')

    def create(self, validated_data):
        validated_data['slug'] = translit(validated_data['title'],'ru', reversed=True)
        return Partners.objects.create(**validated_data)