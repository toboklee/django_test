from django.shortcuts import render
from django.views import generic
from .models import Trip


# Create your views here.
class TripView(generic.ListView):
    template_name = "trip_list.html"

    # Displays 100 most recent trips.
    def get_queryset(self):
        return Trip.objects.all()