from django_filters import rest_framework as filters
from NEWSS.models import NEWSS


class DatesFilter(filters.FilterSet):

    date_of_creation = filters.DateFromToRangeFilter()

    class Meta:
        model = NEWSS
        fields = [
            "date_of_creation",
            "theme",
            "description",
        ]
