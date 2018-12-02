from django.contrib import admin
from basic.models import Course
from django.contrib.sessions.models import Session

admin.site.register(Course)
admin.site.register(Session)
