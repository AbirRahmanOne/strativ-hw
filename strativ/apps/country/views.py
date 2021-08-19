from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

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


class CountryRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()



