from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from base.views import endpoints

urlpatterns = [
    path("", endpoints),
    path('admin/', admin.site.urls),
    path("api/", include("base.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
