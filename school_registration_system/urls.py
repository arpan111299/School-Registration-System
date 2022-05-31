from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('schoolApp.urls')),
    path('api/',include('school_api.urls')),
    # path('customadmin/',include("custom_admin.urls")),
]

schema_view = get_schema_view(
    openapi.Info(
        title='CRUD API',
        default_version="v1",
        description='Test 1'
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)


# urlpatterns += [
#     # ...
#     # Route TemplateView to serve Swagger UI template.
#     #   * Provide `extra_context` with view name of `SchemaView`.
#     path('swagger-ui/', TemplateView.as_view(
#         template_name='swagger_ui.html',
#         extra_context={'schema_url':'openapi-schema'}
#     ), name='api_doc'),
# ]


urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]