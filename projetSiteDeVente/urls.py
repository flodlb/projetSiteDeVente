from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import settings, views


urlpatterns = [
    path('', views.home, name='home'),
    path("admin/", admin.site.urls),
    path("compte/", include("compte.urls")),
    path("application/", include("application.urls"))
]
#Only add when we are in debug mode.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

