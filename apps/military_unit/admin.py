from django.contrib import admin

from apps.military_unit.models import MilitaryUnit, Person, Staff

admin.site.register(MilitaryUnit)
admin.site.register(Person)
admin.site.register(Staff)
