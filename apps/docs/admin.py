from django.contrib import admin
from apps.docs.models import DocTemplate, Docs


@admin.register(Docs)
class DocsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "document_number",
        "person",
        "created_at",
    )
    list_filter = ("created_at",)


admin.site.register(DocTemplate)
