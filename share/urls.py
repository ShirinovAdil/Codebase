from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView

app_name = 'share'

urlpatterns = [
    # Just share
    re_path(r'^$', views.show_code, name="show_code"),
    re_path(r'^AddExercise/$', views.AddExercise.as_view(), name='AddExercise'),

    # Solutions list
    re_path(r'^(?P<pk>\d+)/$', views.code_details, name='code_details'),

    # Shows code of user
    re_path(r'^(?P<some>\d+)/(?P<code_id>\d+)/$', views.personal_code, name='personal_code'),

    # deletes code of user
    re_path(r'^delete_code/(?P<code_id>\d+)$', views.delete_code, name='delete_code'),

    # lets user edit his code
    re_path(r'^(?P<some>\d+)/(?P<code_id>\d+)/edit_current_code/$', views.UpdateCode.as_view(), name='UpdateCode'),

    # add new solution
    re_path(r'^add_new_solution/(?P<ex_id>\d+)/$', views.add_new_solution, name='add_new_solution'),

    # delete problem from list
    re_path(r'^delete/(?P<code_id>\d+)', views.delete_problem),

]
