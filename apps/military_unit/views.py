# form view
from django.views import generic

from apps.military_unit.forms import PersonForm, MilitaryUnitForm
from apps.military_unit.models import Person, MilitaryUnit


class SuccessPage(generic.TemplateView):
    template_name = 'military_unit/success.html'


class PersonView(generic.CreateView):
    model = Person
    form_class = PersonForm
    success_url = "/success/"
    template_name = 'military_unit/person_create.html'


class MilitaryUnitView(generic.CreateView):
    model = MilitaryUnit
    form_class = MilitaryUnitForm
    success_url = "/success/"
    template_name = 'military_unit/military_unit_create.html'
