from django import forms
from.models import PersonalCode, Code


class ShareForm(forms.ModelForm):

    class Meta:
        model = PersonalCode
        fields = ['author_code']


class ShareFormEx(forms.ModelForm):

    class Meta:
        model = Code
        fields = ['title', 'number']

