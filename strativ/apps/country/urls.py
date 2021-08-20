from django.urls  import path

from strativ.apps.country.views import CountryListApiView, CountryRetrieveUpdateDestroyApiView
from . import views


# Api routes
urlpatterns = [

    #Html view route
    path('', views.home, name='home'),
    path('country_search', views.get_country_by_name, name='search_country'),
    path('country_details/<int:pk>', views.country_details, name='country_details'),


    #API View Route
    path('api/countries', CountryListApiView.as_view(), name='country_list'),
    path('api/country/<str:pk>', CountryRetrieveUpdateDestroyApiView.as_view(), name='country'),


]
