from django.urls import path
from apps.military_unit.views import (
    MilitaryUnitView,
)


urlpatterns = [
    path('', MilitaryUnitView.as_view(), name='military_unit_list'),
]
