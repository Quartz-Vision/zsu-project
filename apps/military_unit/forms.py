from datetime import datetime

from django import forms
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

from apps.common.models import City, StreetAddress
from apps.general.models import Position, ReasonType
from apps.docs.models import Docs, DocTemplate
from apps.military_unit.models import Person, MilitaryUnit, Staff
from apps.docs.doc_utils import ContextGenerator, generate_document


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


class AddToThePersonnelForm(forms.Form):
    person = forms.ModelChoiceField(Person.objects.all(), required=True, label=_('Person'))
    position = forms.ModelChoiceField(Position.objects.all(), required=True, label=_('Position'))
    reason = forms.ModelChoiceField(ReasonType.objects.all(), required=True, label=_('Reason Type'))
    document_in = forms.ModelChoiceField(DocTemplate.objects.all(), required=True, label=_('Document In Type'))
    document_number = forms.IntegerField()
    date = DateField(widget=AdminDateWidget)  # TODO: correct calendar widget

    class Meta:
        fields = "__all__"

    def clean(self):
        data = super(AddToThePersonnelForm, self).clean()
        self._handle_personnel_form(data=data)
        return data

    @staticmethod
    def _handle_personnel_form(data: dict) -> None:
        """
        Generate and save document and change a Personnel object
        """
        date: datetime = data.get("date")
        person: Person = data.get('person')
        position: Position = data.get("position")
        reason: ReasonType = data.get("reason")
        template_document: DocTemplate = data.get("document_in")
        document_number = data.get("document_number")
        # Change a Personnel person field
        staff = get_object_or_404(Staff, position=position)
        staff.person = person
        staff.save()
        # Get context for document generation
        context = ContextGenerator.get_extract_from_the_order_context(
            date=date,
            staff=staff,
            person=person,
            reason=reason,
            position=position,
            document_number=document_number,
        )
        # Save document to database
        generated_document: InMemoryUploadedFile = generate_document(
            template=template_document.file, context_data=context
        )
        Docs(
            person=person,
            position=position,
            reason=reason,
            template_document=template_document,
            document_number=document_number,
            date=date,
            file=generated_document,
        ).save()
