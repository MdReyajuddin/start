from django.forms import forms

from start.apps.blog.models import Entry

class EntryForm(forms.ModelForm):
    models = Entry
    fields = '__all__'
