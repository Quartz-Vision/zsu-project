# form view
from django.conf import settings
from django.views import generic

from apps.military_unit.forms import PersonForm, MilitaryUnitForm, AddToThePersonnelForm
from apps.military_unit.models import Person, MilitaryUnit, MilitaryUnitInfo


class PeopleView(generic.TemplateView):
    template_name = 'military_unit/people.html'
    extra_context = {
        "people": Person.objects.all(),
        "host": settings.FRONTEND_HOST
    }


class PersonView(generic.TemplateView):
    template_name = 'military_unit/person.html'
    extra_context = {"host": settings.FRONTEND_HOST}

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if pk is not None:
            person = Person.objects.get(id=pk)
            self.extra_context["person"] = person
        return super(PersonView, self).get(request, *args, **kwargs)


class MilitaryUnitView(generic.TemplateView):
    template_name = 'military_unit/military_unit.html'
    extra_context = {
        "military_unit": MilitaryUnit.objects.all(),
        "host": settings.FRONTEND_HOST
    }


class SuccessPage(generic.TemplateView):
    template_name = 'military_unit/success.html'


class PersonCreateView(generic.CreateView):
    model = Person
    form_class = PersonForm
    success_url = "/add_to_personnel/"
    template_name = 'military_unit/person_create.html'


class MilitaryUnitCreateView(generic.CreateView):
    model = MilitaryUnit
    form_class = MilitaryUnitForm
    success_url = "/success/"
    template_name = 'military_unit/military_unit_create.html'


class AddToThePersonnelView(generic.FormView):
    form_class = AddToThePersonnelForm
    success_url = "/success/"
    template_name = 'military_unit/add_to_personnel.html'
