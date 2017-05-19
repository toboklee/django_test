from rest_framework import serializers
from trips.models import Trip, City, Activity, Accomodation, Transportation
from itertools import chain

class CitySerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()

    class Meta:
        model = City
        fields = ('name', 'country')


class ActivitySerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Activity
        fields = ['name', 'city', 'price']


class TransportationSerializer(serializers.ModelSerializer):
    start_city = CitySerializer()
    end_city = CitySerializer()

    class Meta:
        model = Activity
        fields = ['name', 'start_city', 'end_city', 'price']


class AccomodationSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Activity
        fields = ['name', 'city', 'price']


class TripSerializer(serializers.ModelSerializer):
    activity = ActivitySerializer(many=True)
    transportation = TransportationSerializer(many=True)
    accomodation = AccomodationSerializer(many=True)
    destination = CitySerializer(many=True)
    price = serializers.SerializerMethodField('calc_total')

    def calc_total(self, obj):
        total_price = 0
        currency = ''

        # Combine accomodation, activity and transportation to iterate and calculate the total price.
        # Each service has a threshold (max_people) and after the threshold, price should be calculated
        # from price_diff rather than price.
        services = chain(obj.accomodation.all(), obj.activity.all(), obj.transportation.all())

        for service in services:
            currency = service.price[:1]
            price = float(service.price.replace(',', '')[1:])
            price_diff = float(service.price_diff.replace(',', '')[1:])
            total_price += price * int(service.max_people) + price_diff * (int(obj.max_people) - int(service.max_people))

        return ''.join([currency, str(total_price), ])

    class Meta:
        model = Trip
        fields = [
            'title',
            'description',
            'destination',
            'transportation',
            'activity',
            'accomodation',
            'price',
        ]
