from django import forms
from .models import TaskType, TaskState

class TaskEditForm(forms.Form):
    title = forms.CharField(required=True, max_length=150)
    description = forms.CharField(max_length=500)
    task_type = forms.ModelChoiceField(queryset=TaskState.objects.all())
    #state = forms.ModelChoiceField()
    

class TaskStateChangeForm(forms.Form):
    task_type = forms.ModelChoiceField(queryset=TaskType.objects.all())


class CommentAddForm(forms.Form):
    description = forms.CharField(max_length=500)
