from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    # re_path(r'^map/(?P<latLng>[0-9\._-]+)/$', views.default_map, name="map"),
    path('map/', views.default_map, name="map"),    # has url parameters too
]