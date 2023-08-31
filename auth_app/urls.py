from django import views
from django.conf import settings
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin
from rest_framework import routers
from django.conf.urls.static import static
from .config import API_SECRET_KEY_FOR_SERVER

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include('main.urls')),
    path(API_SECRET_KEY_FOR_SERVER + '/api/users/', include('main.urls.user_urls')),
    path(API_SECRET_KEY_FOR_SERVER + '/api/projects/', include('main.urls.project_urls')),
    path(API_SECRET_KEY_FOR_SERVER + '/api/posts/', include('main.urls.post_urls')),
    #path('api/images/', views.project_views.ImageViewSet.as_view({'get': 'list'}), name='image'),
    #path('auth/', include('djoser.urls')),
    #path('auth/', include('djoser.urls.jwt')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Exclude URLs that start with 'api'
#urlpatterns += [re_path(r'^(?!api).*', TemplateView.as_view(template_name='index.html'))]
