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
    template_name = 'simple_obj/simple_obj_list.html'


class TaskTypeCreate(CreateView):
    model = TaskType
    fields = ['title']
    template_name = 'simple_obj/simple_obj_create_form.html'
    success_url = reverse_lazy('task_types_list')


class TaskTypeUpdate(UpdateView):
    model = TaskType
    fields = ['title']
    template_name = 'simple_obj/simple_obj_update_form.html'
    success_url = reverse_lazy('task_types_list')


class TaskTypeDelete(DeleteView):
    model = TaskType
    success_url = reverse_lazy('task_types_list')
    template_name = 'simple_obj/simple_obj_delete_confirm_form.html'



class TaskStateView(ListView):
    model = TaskState
    template_name = 'simple_obj/simple_obj_list.html'


class TaskStateCreate(CreateView):
    model = TaskState
    fields = ['title']
    template_name = 'simple_obj/simple_obj_create_form.html'
    success_url = reverse_lazy('task_states_list')


class TaskStateUpdate(UpdateView):
    model = TaskState
    fields = ['title']
    template_name = 'simple_obj/simple_obj_update_form.html'
    success_url = reverse_lazy('task_states_list')


class TaskStateDelete(DeleteView):
    model = TaskState
    success_url = reverse_lazy('task_states_list')
    template_name = 'simple_obj/simple_obj_delete_confirm_form.html'