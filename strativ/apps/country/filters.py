from django_filters import FilterSet, CharFilter

from strativ.apps.country.models import Country


# Customize filtering
class CountryFilter(FilterSet):
    def get_neighbouring_country(self, queryset, name, value):
        country = Country.objects.filter(alpha_code3=value)

        if country is None:
            return self.queryset.none()

        return self.queryset.filter(
            alpha_code3__in=country.last().neighbouring_countries
        )

    def get_same_language_country(self, queryset, name, value):
        return self.queryset.filter(
            languages__icontains=value
        )

    name = CharFilter(lookup_expr="icontains")
    neighbouring_country = CharFilter(method='get_neighbouring_country')
    same_language_country = CharFilter(method='get_same_language_country')

    class Meta:
        model = Country
        fields = []
