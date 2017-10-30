from rest_framework.decorators import api_view
from rest_framework.response import Response
from slider.models import Slides
from slider.serializers import SlideSerializer

# Create your views here.


@api_view(['GET'])
def slides_list(request):
    content = Slides.objects.all().filter(show=True)
    serializer = SlideSerializer(content, many=True)
    return Response(serializer.data)
