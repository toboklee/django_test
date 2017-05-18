from rest_framework.generics import ListAPIView
from trips.models import Trip
from .serializers import TripSerializer
from django.db.models import Q


class TripListAPIView(ListAPIView):
    serializer_class = TripSerializer

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        queryset = Trip.objects.all()

        if query:
            # Searching function based on title and destination
            # (supports both city and country).
            queryset = queryset.filter(
                    Q(title__icontains=query)|
                    Q(destination__name__icontains=query)|
                    Q(destination__country__name__icontains=query)
                ).distinct()

        return queryset


