from django.urls  import path

from strativ.apps.country.views import CountryListApiView, CountryRetrieveUpdateDestroyApiView
from . import views
# Api routes
urlpatterns = [
    path('', views.home, name='index'),
    path('country', CountryListApiView.as_view(), name='country_list'),
    path('country/<str:pk>', CountryRetrieveUpdateDestroyApiView.as_view(), name='country_details'),

]
