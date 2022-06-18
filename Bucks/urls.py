<<<<<<< HEAD

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Old Computer Depot'
admin.site.site_title = 'Old Computer Depot'

from Bucks.views import homepage

urlpatterns = [
    path('adminehab/', admin.site.urls),
    path('admin/docs/', include('django.contrib.admindocs.urls')),

    path('',homepage),
    path('repair/', include('repair.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Old Computer Depot'
admin.site.site_title = 'Old Computer Depot'

from Bucks.views import homepage

urlpatterns = [
    path('adminehab/', admin.site.urls),
    path('admin/docs/', include('django.contrib.admindocs.urls')),

    path('',homepage),
    path('repair/', include('repair.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 82835c48c97b5622541c6cb9e52efcec4ece4bb2
