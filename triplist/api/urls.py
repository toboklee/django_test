from django.conf.urls import url
from django.contrib import admin

from .views import TripListAPIView

urlpatterns = [
    url(r'^$', TripListAPIView.as_view(), name="trip_list")
]