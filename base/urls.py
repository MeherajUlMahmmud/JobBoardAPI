from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('auth_control.urls')),
    path('api/user/', include('user_control.urls')),
    path('api/', include('job_control.urls')),
    path('api/', include('exam_control.urls')),
]
