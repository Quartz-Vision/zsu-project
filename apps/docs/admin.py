from django.contrib import admin
from apps.docs.models import DocTemplate, Docs


admin.site.register(DocTemplate)
admin.site.register(Docs)
