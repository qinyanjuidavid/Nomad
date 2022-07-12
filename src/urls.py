from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions  # new
from drf_yasg.views import get_schema_view  # new
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Nomad API",
        default_version="v1",
        description="A Pastrolism API for Nomads around Kenya",
        terms_of_service="https://coderpass.herokuapp.com",
        contact=openapi.Contact(email="davidkinyanjui052@gmail.com"),
        license=openapi.License(name="Day Codes License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('modules.api.urls')),
    path('', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
