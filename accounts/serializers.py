from rest_framework import serializers
from accounts.models import *
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        # user.is_active
        user.save()
        return user


class UserAuthSerializers(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, data):
        return data


class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'avatar', 'description', 'phone_number', 'user', 'created_at', 'updated_at')
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')

    def create(self, validated_data):
        return User.objects.create(**validated_data)
