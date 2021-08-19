from django.urls  import path

from strativ.apps.country.views import CountryListApiView, CountryRetrieveUpdateDestroyApiView
from . import views
# Api routes
urlpatterns = [
    path('', views.home, name='home'),

    path('country_search', views.get_country_name, name='get_name'),
    path('country_details/<int:pk>', views.country_details, name='country_details'),



    path('country', CountryListApiView.as_view(), name='country_list'),
    path('country/<str:pk>', CountryRetrieveUpdateDestroyApiView.as_view(), name='country'),


]
