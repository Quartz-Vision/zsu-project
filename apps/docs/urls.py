from django.urls import path
from apps.docs.views import (
    IncomingDocumentsView,
)


urlpatterns = [
    path('docs/incoming/', IncomingDocumentsView.as_view(), name='incoming_documents'),
]
