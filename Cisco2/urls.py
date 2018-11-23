from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('personal.urls')),
    re_path(r'^accounts/', include("accounts.urls")),
    re_path(r'^share/', include("Share.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
