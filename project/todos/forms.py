from django import forms
from .models import Todo


class TodoForm(forms.Form):

    title = forms.CharField()
    description = forms.CharField()


class TodoModelForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'description']