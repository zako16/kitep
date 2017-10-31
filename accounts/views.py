from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view, detail_route, permission_classes
from rest_framework.response import Response
from accounts.models import *
from accounts.serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from accounts.email_confirmation import EmailSender


class UserSignupView(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            # serializer.se
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserSignInView(APIView):
    # permission_classes()
    @csrf_exempt
    def post(self, request, format=None):
        serializer = UserAuthSerializers(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        # username = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(username=username, password=password)
        # # if serializer.is_valid():
        # #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if user is not None:
        #     if user.is_active:
        #         login(request, user)
        #         return redirect('/')
        #     else:
        #         context = {'login_error': 'Пользователь не найден'}
        # else:
        #     context = {'login_error': 'Пароль или логин неправильны'}
        # return Response(status=status.HTTP_400_BAD_REQUEST)


class EmailConfirmationView(APIView):
    def get(self):
        pass

    @csrf_exempt
    def post(self, request, format=None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            EmailSender(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
