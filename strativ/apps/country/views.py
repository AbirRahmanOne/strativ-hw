from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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


def home(request):
    countries = Country.objects.all()
    # Filtering search button
    myFilter = CountryFilter(request.GET, queryset=countries)
    # page = request.GET.get('page',1)
    #
    # paginator = Paginator(country_list, 10)
    # try:
    #     countries = paginator.page(page)
    # except PageNotAnInteger:
    #     countries = paginator.page(1)
    # except EmptyPage:
    #     countries = paginator.page(paginator.num_pages)
    context= { 'countries': countries, 'myFilter': myFilter}
    return render(request, 'country/home.html', context)
