from django.views import generic

from apps.docs.models import DocTemplate
from apps.military_unit.forms import PersonForm, MilitaryUnitForm, AddToThePersonnelForm
from apps.military_unit.models import Person, MilitaryUnit


class SuccessPage(generic.TemplateView):
    template_name = 'military_unit/success.html'


class PersonView(generic.CreateView):
    model = Person
    form_class = PersonForm
    success_url = "/add_to_personnel/"
    template_name = 'military_unit/person_create.html'


class MilitaryUnitView(generic.CreateView):
    model = MilitaryUnit
    form_class = MilitaryUnitForm
    success_url = "/success/"
    template_name = 'military_unit/military_unit_create.html'


class AddToThePersonnelView(generic.FormView):
    form_class = AddToThePersonnelForm
    success_url = "/success/"
    template_name = 'military_unit/add_to_personnel.html'

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
