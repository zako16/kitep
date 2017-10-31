from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view, detail_route, permission_classes
from rest_framework.response import Response
from books.models import *
from books.serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.contrib.auth.models import User


class BooksListView(APIView):
    def get(self, request, **kwargs):
        content = Books.objects.all().filter(is_issue=True)
        serializer = BooksListSerializers(content, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = BooksListSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, is_issue=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class BooksListByCategoryView(APIView):
    def get(self, request, category_id, *args, **kwargs):
        category = Categories.objects.get(id=category_id)
        content = category.books_set.all().filter(is_issue=True)
        serializer = BooksListSerializers(content, many=True)
        return Response(serializer.data)


class BooksListByYearView(APIView):
    def get(self, request, year, *args, **kwargs):
        year = Years.objects.get(year=year)
        content = year.books_set.all().filter(is_issue=True)
        serializer = BooksListSerializers(content, many=True)
        return Response(serializer.data)


class BooksListByUserView(APIView):
    def get(self, request, username, *args, **kwargs):
        if request.user == username or request.user.is_staff:
            content = Books.objects.all().filter(user=username)
            serializer = BooksListSerializers(content, many=True)
            return Response(serializer.data)
        content = Books.objects.all().filter(user=username, is_issue=True)
        serializer = BooksListSerializers(content, many=True)
        return Response(serializer.data)


class BooksView(APIView):
    def get_object(self, book_id):
        try:
            return Books.objects.get(id=book_id)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request, book_id, *args, **kwargs):
        content = self.get_object(book_id)
        if content.is_issue is True:
            serializer = BooksDetailSerializers(content)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            if request.user == content.user or request.user.is_staff:
                serializer = BooksDetailSerializers(content)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_403_FORBIDDEN)


    @csrf_exempt
    @permission_classes('is_authenticated', )
    def put(self, request, book_id, *args, **kwargs):
        content = self.get_object(book_id)
        if request.user == content.user:
            serializer = BooksDetailSerializers(content, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(user=content.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)


    @csrf_exempt
    @permission_classes('is_authenticated', )
    def delete(self, request, book_id):
        content = self.get_object(book_id)
        if request.user == content.user:
            content.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)


class CategoriesListView(APIView):
    def get(self, request, **kwargs):
        content = Categories.objects.all()
        serializer = CategoriesSerializers(content, many=True)
        return Response(serializer.data)

    @csrf_exempt
    @permission_classes('is_authenticated', )
    def post(self, request, format=None):
        serializer = CategoriesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class YearsListViews(APIView):
    def get(self, request, *args, **kwargs):
        content = Years.objects.all()
        serializer = YearsSerializers(content, many=True)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        ch = Years.objects.all()
        if request.user.is_superuser and ch is None:
            for year in range(1900, 2018):
                obj = Years.objects.create(year=year)
                obj.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class PublishersListView(APIView):
    def get(self, request):
        content = Publisher.objects.all()
        serializer = PublishersSerializers(content, many=True)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class StatusesListView(APIView):
    def get(self, request):
        content = Statuses.objects.all()
        serializer = StatusesSerializers(content, many=True)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class CoverTypesListView(APIView):
    def get(self, request):
        content = CoverTypes.objects.all()
        serializer = CoverTypesSerizlizers(content, many=True)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)