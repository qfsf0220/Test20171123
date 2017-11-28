"""Test20171123 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from test1126 import views as test1126views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',test1126views.index),
    url(r'^add/(\d+)/(\d+)/$',test1126views.add,name="add"),
    url(r'^info',test1126views.info,name="info"),
    url(r'^add2',test1126views.add2,name="add2"),
    url(r'^home2',test1126views.home2,name="home2")
]
