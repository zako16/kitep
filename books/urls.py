from django.conf.urls import url
from books.views import *
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.SimpleRouter()

urlpatterns = [
    url(r'^$', BooksListView.as_view(), name='books'),
    url(r'^(?P<book_id>[0-9]+)/$', BooksView.as_view(), name='book_detail'),
    url(r'^categories/(?P<category_id>\w+)/$', BooksListByCategoryView.as_view(), name='by_category_list'),
    url(r'^categories/$', CategoriesListView.as_view(), name='categories'),
    url(r'^years/$', YearsListViews.as_view(), name='years'),
    url(r'^years/(?P<year>[0-9]{4})/$', BooksListByYearView.as_view(), name='by_years_list'),
    url(r'^statuses/$', StatusesListView.as_view(), name='statuses'),
    url(r'^covertypes/$', CoverTypesListView.as_view(), name='cover_types'),
    url(r'^publishers/$', PublishersListView.as_view(), name='publishers'),
    url(r'^users/(?P<username>\w+)/$', BooksListByUserView.as_view(), name='by_user_list'),
]

urlpatterns += router.urls
urlpatterns = format_suffix_patterns(urlpatterns)
