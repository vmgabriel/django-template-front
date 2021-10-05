"""Django Config APP Urls"""

# Libraries
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),

    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),

    path("cameras/", include("cameras.urls")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
