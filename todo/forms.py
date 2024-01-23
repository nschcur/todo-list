from django import forms
from django.core.exceptions import ValidationError
from .models import Tag, Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
                    "placeholder": "Search by date",
                    "type": "datetime-local",
            }
        )
    )

    class Meta:
        model = Task
        fields = ("content", "tags", "deadline")