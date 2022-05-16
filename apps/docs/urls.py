from django.urls import path
from apps.docs.views import (
    IncomingDocumentsView,
    OutputDocumentsView,
)


urlpatterns = [
    path('docs/incoming/', IncomingDocumentsView.as_view(), name='incoming_documents'),
    path('docs/output/', OutputDocumentsView.as_view(), name='output_documents'),
]
