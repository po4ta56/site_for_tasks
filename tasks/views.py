from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *

class TasksView(ListView):
    model = Task
    template_name = 'tasks_list.html'


class TaskTypeCreate(CreateView):
    model = TaskType
    fields = ['title']


class TaskTypeUpdate(UpdateView):
    model = TaskType
    fields = ['title']


class TaskTypeDelete(DeleteView):
    model = TaskType
    success_url = reverse_lazy('task_type_list')