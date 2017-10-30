"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from partners.views import *
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    url(r'^$', partners_list, name='partners'),
    # url(r'^create/$', partner_create, name='partner_create'),
    url(r'^(?P<partner_id>[0-9])/$', partner_detail, name='partner_create'),
]
urlpatterns += router.urls