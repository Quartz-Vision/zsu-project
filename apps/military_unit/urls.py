from django.urls import path

from apps.docs import urls
from apps.military_unit.views import (
    MilitaryUnitView,
    PersonCreateView,
    SuccessPage,
    AddToThePersonnelView,
    PeopleView,
    PersonView,
    MilitaryUnitCreateView,
    StaffView, MilitaryUnitInfoView,
)


urlpatterns = [
    path('', PersonCreateView.as_view(), name='person_create'),
    path('people/', PeopleView.as_view(), name='people'),
    path('people/<uuid:pk>/', PersonView.as_view(), name='person'),
    path('staff/', StaffView.as_view(), name='staff'),
    path('military/', MilitaryUnitView.as_view(), name='military_unit_list'),
    path('military/<uuid:pk>/', MilitaryUnitInfoView.as_view(), name='military_unit_info'),
    path('military_create/', MilitaryUnitCreateView.as_view(), name='military_unit_create'),
    path('add_to_personnel/', AddToThePersonnelView.as_view(), name='add_to_personnel'),
    path('success/', SuccessPage.as_view(), name='success')
]

urlpatterns += urls.urlpatterns
