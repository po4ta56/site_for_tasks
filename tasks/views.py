from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *

class TasksView(ListView):
    model = Task
    template_name = 'tasks_list.html'


class TaskTypesView(ListView):
    model = TaskType
    template_name = 'task_types/task_types_list.html'


class TaskTypeCreate(CreateView):
    model = TaskType
    fields = ['title']
    template_name = 'task_types/task_type_create_form.html'
    success_url = reverse_lazy('task_types_list')


class TaskTypeUpdate(UpdateView):
    model = TaskType
    fields = ['title']
    template_name = 'task_types/task_type_update_form.html'
    success_url = reverse_lazy('task_types_list')


class TaskTypeDelete(DeleteView):
    model = TaskType
    success_url = reverse_lazy('task_types_list')
    template_name = 'task_types/task_type_delete_confirm_form.html'