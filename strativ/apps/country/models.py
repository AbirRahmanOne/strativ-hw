from django.db import models

# Country Model


class Country(models.Model):

    name = models.CharField(max_length=120)
    alpha_code2 = models.CharField(max_length=20)
    alpha_code3 = models.CharField(max_length=20, unique=True)
    capital = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    timezones = models.JSONField()
    flag = models.URLField(blank=True, null=True)
    languages = models.JSONField()
    neighbouring_countries = models.JSONField()

    def __str__(self):
        return self.name




