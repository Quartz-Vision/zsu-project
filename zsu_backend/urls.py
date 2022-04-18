from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


urlpatterns = [
    path('watch-tower/', admin.site.urls),
    path('', include('apps.military_unit.urls')),
]


if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title="ZSU API",
            default_version='v1',
            description="ZSU for the data management",
        ),
        permission_classes=(permissions.AllowAny,),
        public=True,
    )

    urlpatterns += [
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
        path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
    ]
