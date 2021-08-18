from django.urls  import path

from strativ.apps.country.views import CountryListApiView, CountryRetrieveUpdateDestroyApiView

# Api routes
urlpatterns = [
    path('country', CountryListApiView.as_view(), name='country_list'),
    path('country/<str:pk>', CountryRetrieveUpdateDestroyApiView.as_view(), name='country_details'),

]
