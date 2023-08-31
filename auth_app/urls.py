from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from .config import API_SECRET_KEY_FOR_SERVER

urlpatterns = [
    path('admin/', admin.site.urls),

   path(API_SECRET_KEY_FOR_SERVER + 'api/users/', include('main.urls.user_urls')),
    path(API_SECRET_KEY_FOR_SERVER + 'api/projects/', include('main.urls.project_urls')),
    path(API_SECRET_KEY_FOR_SERVER + 'api/posts/', include('main.urls.post_urls')),
    path(API_SECRET_KEY_FOR_SERVER + 'api/jobs/', include('main.urls.job_urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

