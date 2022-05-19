from django.conf import settings
from django.views import generic

from apps.docs.models import DocTemplate, Docs
from apps.military_unit.models import Person


class IncomingDocumentsView(generic.TemplateView):
    template_name = 'docs/incoming_docs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incoming_documents'] = DocTemplate.objects.all()
        context["host"]: settings.FRONTEND_HOST
        return context


class OutputDocumentsView(generic.TemplateView):
    template_name = 'docs/output_documents.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['output_documents'] = Docs.objects.all()
        context["host"]: settings.FRONTEND_HOST
        return context


class DocumentView(generic.TemplateView):
    template_name = 'docs/doc_preview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["host"] = settings.FRONTEND_HOST
        context["media"] = settings.MEDIA_URL
        pk = self.kwargs.get("pk", None)
        if pk is not None:
            person = Person.objects.filter(id=pk)
            if person:
                full_name = f"{person.last_name} {person.middle_name} {person.first_name}"
                doc_list = Docs.objects.filter(name=full_name)
                context['doc'] = doc_list.first().file
            else:
                doc = Docs.objects.get(id=pk)
                context['doc'] = doc.file
        return context

