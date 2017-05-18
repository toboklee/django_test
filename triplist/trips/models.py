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


class Trip(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, null=False)
    max_people = models.IntegerField(default=1, null=False)
    trip_start_at = models.DateTimeField(verbose_name='StartAt', null=False)
    trip_end_at = models.DateTimeField(verbose_name='EndAt', null=False)
    destination = models.ManyToManyField(City)
    price = models.CharField(max_length=15, null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='CreatedAt', null=False)
    last_modified_at = models.DateTimeField(auto_now_add=True, verbose_name='ModifiedAt', null=False)


    def __str__(self):
        return ' - '.join([self.title, self.description,])

