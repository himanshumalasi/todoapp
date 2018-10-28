from django import forms
from .models import TodoList

class ListItem(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['name','completed']


