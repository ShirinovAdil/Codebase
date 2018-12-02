from django.urls import re_path
from .views import HomeForm
from share.views import show_users_list

app_name = "basic"

urlpatterns = [
    re_path(r'^$', HomeForm.as_view(), name="HomeForm"),
    re_path(r'show_users_list/$', show_users_list, name='show_users_list')
]
