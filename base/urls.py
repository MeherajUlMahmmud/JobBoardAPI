from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

schema_view = get_schema_view(
    openapi.Info(
        title="Job Portal API",
        default_version='v1',
        description="Job Portal API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@jobboard.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

from user_control.urls import router as user_router

router = routers.DefaultRouter()
router.registry.extend(user_router.registry)

urlpatterns = [
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/', include('auth_control.urls')),
    path('api/', include('user_control.urls')),
    path('api/', include('job_control.urls')),
    path('api/', include('resume_control.urls')),
]
