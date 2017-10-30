from django.shortcuts import render
from partners.models import Partners
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from partners.serializers import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@api_view(['GET'])
def partners_list(request):
    content = Partners.objects.all()
    serializer = PartnersSerializers(content, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def partner_detail(request, partner_id):
    content = Partners.objects.get(id=partner_id)
    serializer = PartnersDetailSerializers(content, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@csrf_exempt
def partner_create(request):
    serializer = PartnersModelSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)