from django.conf import settings
from django.views import generic

from apps.docs.models import DocTemplate, Docs


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
