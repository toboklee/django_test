from rest_framework import serializers
from trips.models import Trip


class TripSerializer(serializers.ModelSerializer):
    destination = serializers.StringRelatedField(many=True)

    class Meta:
        model = Trip
        fields = [
            'title',
            'description',
            'destination',
            'price',
        ]
