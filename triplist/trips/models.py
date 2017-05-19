from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, null=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    country = models.ForeignKey(Country, related_name='country')

    def __str__(self):
        return ' - '.join([self.name, self.country.name,])


# travelers <= max_people, regular price;
# travelers > max_people, price_diff.
class Transportation(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.CharField(max_length=100, null=False)
    max_people = models.CharField(max_length=100, null=True)
    price_diff = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=50, null=False)
    start_city = models.ForeignKey(City, related_name='transportation.start_city', null=True)
    end_city = models.ForeignKey(City, related_name='transportation.end_city', null=True)

    def __str__(self):
        return ' - '.join([self.name, self.type, ])


# travelers <= max_people, regular price;
# travelers > max_people, price_diff.
class Accomodation(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    city = models.ForeignKey(City, related_name='accomodation.city')
    price = models.CharField(max_length=100, null=False)
    max_people = models.CharField(max_length=100, null=True)
    price_diff = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=50, null=False)

    def __str__(self):
        return ' - '.join([self.name, self.type, self.city.name,])


# travelers <= max_people, regular price;
# travelers > max_people, price_diff.
class Activity(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.CharField(max_length=100, null=False)
    max_people = models.CharField(max_length=100, null=True)
    price_diff = models.CharField(max_length=100, null=True)
    city = models.ForeignKey(City, related_name='activity.city')

    def __str__(self):
        return ' - '.join([self.name, self.price,])


class Trip(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, null=False)
    max_people = models.IntegerField(default=1, null=False)
    trip_start_at = models.DateTimeField(verbose_name='StartAt', null=False)
    trip_end_at = models.DateTimeField(verbose_name='EndAt', null=False)
    destination = models.ManyToManyField(City)
    activity = models.ManyToManyField(Activity)
    accomodation = models.ManyToManyField(Accomodation)
    transportation = models.ManyToManyField(Transportation)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='CreatedAt', null=False)
    last_modified_at = models.DateTimeField(auto_now_add=True, verbose_name='ModifiedAt', null=False)


    def __str__(self):
        return ' - '.join([self.title, self.description,])

