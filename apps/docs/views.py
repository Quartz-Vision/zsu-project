from django.conf import settings
from django.views import generic

from apps.docs.models import DocTemplate


class IncomingDocumentsView(generic.TemplateView):
    template_name = 'docs/incoming_docs.html'
    extra_context = {
        "incoming_documents": DocTemplate.objects.all(),
        "host": settings.FRONTEND_HOST
    }
