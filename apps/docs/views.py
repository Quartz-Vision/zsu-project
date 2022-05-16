from django.conf import settings
from django.views import generic

from apps.docs.models import DocTemplate, Docs


class IncomingDocumentsView(generic.TemplateView):
    template_name = 'docs/incoming_docs.html'
    extra_context = {
        "incoming_documents": DocTemplate.objects.all(),
        "host": settings.FRONTEND_HOST
    }


class OutputDocumentsView(generic.TemplateView):
    template_name = 'docs/output_documents.html'
    extra_context = {
        "output_documents": Docs.objects.all(),
        "host": settings.FRONTEND_HOST
    }
