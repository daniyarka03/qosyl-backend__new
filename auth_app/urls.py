from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('main.urls.user_urls')),
    path('api/projects/', include('main.urls.project_urls')),
    path('api/posts/', include('main.urls.post_urls')),
    path('api/jobs/', include('main.urls.job_urls')),
    path('api/students_clubs/', include('main.urls.students-club_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

