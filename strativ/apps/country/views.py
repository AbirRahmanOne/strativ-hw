from django.shortcuts import render, HttpResponse, redirect
from django_filters.rest_framework import DjangoFilterBackend
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from strativ.apps.country.models import Country
from strativ.apps.country.serializers import CountrySerializer

from strativ.apps.country.filters import CountryFilter


# Create your views here.


class CountryListApiView(ListCreateAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_class = CountryFilter
    permission_classes = [IsAuthenticated]


class CountryRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    permission_classes = [IsAuthenticated]


def home(request):
    countries = Country.objects.all()
    context = {'countries': countries}
    return render(request, 'country/home.html', context)


def get_country_by_name(request):
    search_key = request.GET['value']
    countries = Country.objects.filter(name__startswith=search_key)
    context = {'countries': countries}
    return render(request, 'country/home.html', context)


def country_details(request, pk):

    country = Country.objects.get(id=pk)
    neighbouring_countries = []
    # find the neighbouring countries name
    for alphacode3 in country.neighbouring_countries:
        cur_country = Country.objects.filter(alpha_code3=alphacode3).values('name', 'languages').first()
        neighbouring_countries.append(cur_country)

    context = { 'country': country, 'neighbours': neighbouring_countries }

    return render(request, 'country/details.html', context)


def login(request):
    pass