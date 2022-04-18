from django import forms
from apps.military_unit.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
