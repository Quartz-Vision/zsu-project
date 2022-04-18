#form view
from django.shortcuts import render
from django.views import generic

from apps.military_unit.models import Person
from apps.military_unit.forms import PersonForm


# Create your views here.
class MilitaryUnitView(generic.FormView):
    model = Person
    form_class = PersonForm
    template_name = 'military_unit/military_unit_create.html'
