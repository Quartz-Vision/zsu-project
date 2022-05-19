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
            person = Person.objects.filter(id=pk).first()
            if person:
                document = Docs.objects.filter(person=person).first()
                context['doc'] = document.file
            else:
                doc = Docs.objects.get(id=pk)
                context['doc'] = doc.file
        return context

