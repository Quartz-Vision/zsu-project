from re import S
from django.contrib import admin
from apps.common.models import(
    City,
    StreetAddress,
)

admin.site.register(City)
admin.site.register(StreetAddress)
