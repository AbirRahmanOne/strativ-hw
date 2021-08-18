import requests
from django.core.management.base import BaseCommand

# importing Country model
from strativ.apps.country.models import Country

# Api urls
base_url = 'https://restcountries.eu/rest/v2/all'


def add_countries():
    response = requests.get(base_url)

    # Error Handler
    if response.status_code != 200:
        return 0

    countries_data = response.json()

    for data in countries_data:
        country = Country(
            name=data['name'],
            alpha_code2=data['alpha2Code'],
            alpha_code3=data['alpha3Code'],
            capital=data['capital'],
            population=data['population'],
            neighbouring_countries=data['borders'],
            timezones=data['timezones'],
            flag=data['flag'],
            languages=[language["name"] for language in data['languages']],

        )
        country.save()
        total_add_countries = Country.objects.all()

    return len(total_add_countries)


def clear_data():
    Country.objects.all().delete()


class Command(BaseCommand):

    def handle(self, *args, **options):
        # clear_data()
        total_countries = add_countries()
        print(f"Successfully added, {total_countries} data.")
