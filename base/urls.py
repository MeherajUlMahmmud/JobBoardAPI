from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from common.views import IndexView

schema_view = get_schema_view(
    openapi.Info(
        title="JobBoard API",
        default_version='v1',
        description="JobBoard API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@jobboard.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
    urlconf='base.urls',
)

router = routers.DefaultRouter()

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/', IndexView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/', include('auth_control.urls')),
    path('api/', include('user_control.urls')),
    path('api/', include('resume_control.urls')),
    path('api/', include('job_control.urls')),
    path('api/', include('test_control.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
