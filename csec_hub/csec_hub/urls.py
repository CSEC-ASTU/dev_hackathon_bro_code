"""csec_hub URL Configuration
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 

    path('',include('core.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    
    path('summernote/', include('django_summernote.urls')),
 
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

