from django.conf.urls import url
from accounts.views import *
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.SimpleRouter()

urlpatterns = [
    url(r'signup/^$', UserSignupView.as_view(), name='signup'),
    url(r'signin/^$', UserSignInView.as_view(), name='signin'),
]

urlpatterns += router.urls
urlpatterns = format_suffix_patterns(urlpatterns)
