from django.views import generic
from .models import Trip


class TripView(generic.ListView):
    template_name = "trip_list.html"

    def get_queryset(self):
        return Trip.objects.all()