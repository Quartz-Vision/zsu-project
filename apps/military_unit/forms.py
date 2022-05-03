from django import forms
from django.utils.translation import gettext_lazy as _

from apps.common.models import City, StreetAddress
from apps.military_unit.models import Person, MilitaryUnit


class AddressForm(forms.ModelForm):
    city = forms.ModelChoiceField(City.objects.all(), required=True, label=_('City'))

    class Meta:
        model = StreetAddress
        fields = "__all__"


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
            'position',
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

    def clean(self):
        data = super(PersonForm, self).clean()
        street_address = StreetAddress.objects.create(
            city=data.get("city"),
            name=data.get("address"),
        )
        data["address"] = street_address
        return data


class MilitaryUnitForm(forms.ModelForm):
    city = forms.ModelChoiceField(City.objects.all(), required=True, label=_('City'))
    address = forms.CharField(max_length=255, required=True, label=_('Address'))

    class Meta:
        model = MilitaryUnit
        fields = (
            'name',
            'military_number',
            'city',
            'address',
        )

    def clean(self):
        data = super(MilitaryUnitForm, self).clean()
        street_address = StreetAddress.objects.create(
            city=data.get("city"),
            name=data.get("address"),
        )
        data["address"] = street_address
        return data
