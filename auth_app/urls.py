from django.urls import path, include, re_path
from django.views.generic import TemplateView

from main import admin

urlpatterns = [
    path('api/', include('main.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

# Exclude URLs that start with 'api'
urlpatterns += [re_path(r'^(?!api).*', TemplateView.as_view(template_name='index.html'))]