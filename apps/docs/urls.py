from django.urls import path
from apps.docs.views import (
    IncomingDocumentsView,
    OutputDocumentsView,
    DocumentView,
)


urlpatterns = [
    path('docs/incoming/', IncomingDocumentsView.as_view(), name='incoming_documents'),
    path('docs/output/', OutputDocumentsView.as_view(), name='output_documents'),
    path('docs/preview/<uuid:pk>/', DocumentView.as_view(), name='doc_preview'),
]
