from django import forms
from django.forms import ModelChoiceField
from personal.models import Course


class CourseFormField(ModelChoiceField):

    def label_from_instance(self, obj):
        return obj.course_name


class NewForm(forms.Form):
    choice = CourseFormField(queryset=Course.objects.all(), required=True, label="Course name", empty_label=None)


