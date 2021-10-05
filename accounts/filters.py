"""All Filters of Accounts"""

# Libraries
import django_filters

# Models
from .models import User


class ProfileFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(label="First Name", lookup_expr="icontains")
    last_name = django_filters.CharFilter(label="Last Name", lookup_expr="icontains")
    username = django_filters.CharFilter(label="Username", lookup_expr="icontains")
    telephone = django_filters.CharFilter(label="Telephone", lookup_expr="icontains")
    active = django_filters.BooleanFilter(field_name="inactive_at", label="Is Active", lookup_expr="isnull")
    sort = django_filters.OrderingFilter(
        fields=(
            ("username", "Username"),
            ("first_name", "First Name"),
            ("last_name", "Last Name"),
            ("telephone", "Telephone")
        ),
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "telephone", "active"]
