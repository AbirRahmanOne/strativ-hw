from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from strativ.apps.country.models import Country
from strativ.apps.country.serializers import CountrySerializer

from strativ.apps.country.filters import CountryFilter

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


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


@login_required(login_url='login')
def home(request):
    countries = Country.objects.all()
    context = {'countries': countries}
    return render(request, 'country/home.html', context)


@login_required(login_url='login')
def get_country_by_name(request):
    search_key = request.GET['value']
    countries = Country.objects.filter(name__startswith=search_key)
    context = {'countries': countries}
    return render(request, 'country/home.html', context)


@login_required(login_url='login')
def country_details(request, pk):

    country = Country.objects.get(id=pk)
    neighbouring_countries = []
    # find the neighbouring countries name
    for alphacode3 in country.neighbouring_countries:
        cur_country = Country.objects.filter(alpha_code3=alphacode3).values('name', 'languages').first()
        neighbouring_countries.append(cur_country)

    context = { 'country': country, 'neighbours': neighbouring_countries }

    return render(request, 'country/details.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, "Incorrect User")

    context = {}
    return render(request, 'country/login.html', context)