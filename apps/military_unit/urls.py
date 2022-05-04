from django.urls import path
from apps.military_unit.views import (
    MilitaryUnitView,
    PersonView,
    SuccessPage,
)


urlpatterns = [
    path('', PersonView.as_view(), name='person_create'),
    path('military/', MilitaryUnitView.as_view(), name='military_unit_list'),
    path('success/', SuccessPage.as_view(), name='success')
]
