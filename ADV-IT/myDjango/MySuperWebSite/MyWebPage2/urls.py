from django.conf.urls import include
from django.urls import re_path
from . import views
app_name = "a"

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]