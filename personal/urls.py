from django.urls import re_path
from .views import HomeForm

app_name = "personal"

urlpatterns = [
    re_path(r'^$', HomeForm.as_view(), name="HomeForm"),
]
