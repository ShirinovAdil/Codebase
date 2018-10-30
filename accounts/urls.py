from django.urls import path, re_path
from . import views
app_name = 'accounts'

urlpatterns = [
    re_path(r'^$', views.index_page, name="index_page"),
    re_path(r'^login/$', views.login_view, name='login'),
    re_path(r'^logout/$', views.logout_view, name='logout'),
    re_path(r'^register/$', views.register, name="register"),
    re_path(r'^profile/$', views.profile, name="profile"),
    re_path(r'^profile/edit/$', views.edit_profile, name="edit_profile"),
    re_path(r'^change-password/$', views.change_password, name="change_password"),
]


