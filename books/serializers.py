from rest_framework import serializers
from books.models import *
from django.contrib.auth.models import User
from transliterate import translit, get_available_language_codes

# Books Serializers


class BooksListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'title', 'author', 'cover', 'category', 'description', 'year', 'coverType', 'publisher',
                  'status', 'exchange', 'sale', 'price', 'user', 'created_at', 'updated_at', 'is_issue')
        read_only_fields = ('id', 'user', 'created_at', 'updated_at', 'is_issue')

    def create(self, validated_data):
        return Books.objects.create(**validated_data)


class BooksDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'title', 'author', 'cover', 'category', 'description', 'year', 'coverType', 'publisher',
                  'status', 'exchange', 'sale', 'price', 'user', 'created_at', 'updated_at', 'is_issue')
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')


# Other Serializers


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'title', 'slug')

    def create(self, validated_data):
        return Categories.objects.create(**validated_data)


class YearsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Years
        fields = ('id', 'year')
        read_only_fields = ('id', 'year')


class PublishersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'title')


class StatusesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        fields = ('id', 'status')
        read_only_fields = ('id', 'status')


class CoverTypesSerizlizers(serializers.ModelSerializer):
    class Meta:
        model = CoverTypes
        fields = ('id', 'type')