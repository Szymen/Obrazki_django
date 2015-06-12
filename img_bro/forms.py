__author__ = 'szymon'

from django import forms

class AddNewForm(forms.Form):
    new_name = forms.CharField(max_length = 100)
    new_source = forms.CharField(max_length = 100)
