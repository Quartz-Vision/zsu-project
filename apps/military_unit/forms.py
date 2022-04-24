from django import forms
from django.utils.translation import gettext_lazy as _

from apps.common.models import City
from apps.military_unit.models import Person


class PersonForm(forms.ModelForm):
    city = forms.ModelChoiceField(City.objects.all(), required=True, label=_('City'))
    address = forms.CharField(max_length=255, required=True, label=_('Address'))

    class Meta:
        model = Person
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'gender',
            'birth_date',
            'city',
            'address',
            'family_status',
            'children_number',
            'phone_number',
            'tin',
            'recruitment_office',
            'military_rank',
            'military_specialization',
            'length_of_service',
            'contract_term',
        )
