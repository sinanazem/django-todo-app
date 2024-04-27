from django import forms
from home.models import Todo

class TodoCreateForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    date = forms.DateTimeField()
    completed = forms.BooleanField()


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("title", "description", "date")
