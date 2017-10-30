from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from news.models import News
from news.serializers import NewsSerializers, NewsDetailSerializers
# Create your views here.


@api_view(['GET'])
def news_list(request):
    if request.method == 'GET':
        content = News.objects.all()
        serializer = NewsSerializers(content, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def news_detail(request, news_id):
    if request.method == 'GET':
        content = News.objects.get(id=news_id)
        serializer = NewsDetailSerializers(content, many=False)
        return Response(serializer.data)
