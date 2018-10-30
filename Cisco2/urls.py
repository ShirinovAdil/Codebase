from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('personal.urls')),
    re_path(r'^accounts/', include("accounts.urls")),
    re_path(r'^share/', include("Share.urls")),
]
