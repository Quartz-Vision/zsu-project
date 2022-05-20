# form view
from django.conf import settings
from django.views import generic
from django.urls import reverse

from apps.docs.models import DocTemplate
from apps.military_unit.forms import PersonForm, MilitaryUnitForm, AddToThePersonnelForm
from apps.military_unit.models import Person, MilitaryUnit, MilitaryUnitInfo, Staff


class StaffView(generic.TemplateView):
    template_name = 'military_unit/staff.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff'] = Staff.objects.all()
        context["host"]: settings.FRONTEND_HOST
        return context


class PeopleView(generic.TemplateView):
    template_name = 'military_unit/people.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['people'] = Person.objects.all()
        context["host"]: settings.FRONTEND_HOST
        return context


class PersonView(generic.TemplateView):
    template_name = 'military_unit/person.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["host"]: settings.FRONTEND_HOST
        pk = self.kwargs.get("pk", None)
        if pk is not None:
            person = Person.objects.get(id=pk)
            context["person"] = person
        return context


class MilitaryUnitView(generic.TemplateView):
    template_name = 'military_unit/military_unit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['military_unit'] = MilitaryUnitInfo.objects.all()
        context["host"]: settings.FRONTEND_HOST
        return context


class MilitaryUnitInfoView(generic.TemplateView):
    template_name = 'military_unit/military_unit_info.html'
    extra_context = {
        "host": settings.FRONTEND_HOST
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["host"]: settings.FRONTEND_HOST
        pk = self.kwargs.get("pk", None)
        if pk is not None:
            military_unit_info = MilitaryUnitInfo.objects.get(id=pk)
            context["military_unit_info"] = military_unit_info
        return context


class SuccessPage(generic.TemplateView):
    template_name = 'military_unit/success.html'


class PersonCreateView(generic.CreateView):
    model = Person
    form_class = PersonForm
    success_url = "/add_to_personnel/"
    template_name = 'military_unit/person_create.html'

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial_data: dict = {
            "vacation_days": 0,
        }
        return initial_data


class MilitaryUnitCreateView(generic.CreateView):
    model = MilitaryUnit
    form_class = MilitaryUnitForm
    success_url = "/success/"
    template_name = 'military_unit/military_unit_create.html'


class AddToThePersonnelView(generic.FormView):
    form_class = AddToThePersonnelForm
    template_name = 'military_unit/add_to_personnel.html'

    def get_success_url(self):
        person_id = self.request.POST.get('person')
        return reverse("doc_preview", kwargs={"pk": person_id})

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        try:
            document_template = DocTemplate.objects.get(name="ExtractFromTheOrder")
            initial_data: dict = {
                "document_in": document_template,
            }
            return initial_data
        except DocTemplate.DoesNotExist:
            return {}
