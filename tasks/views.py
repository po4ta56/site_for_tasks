from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import *
from .forms import *



class TasksView(LoginRequiredMixin, ListView):  
    model = Task
    template_name = 'tasks_list.html'
    redirect_field_name = 'redirect_to'



class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'task_type', 'description']
    template_name = 'simple_obj/simple_obj_create_form.html'
    success_url = reverse_lazy('task_list')



class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'task_type', 'description']
    template_name = 'simple_obj/simple_obj_update_form.html'
    success_url = reverse_lazy('task_list')



class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    template_name = 'simple_obj/simple_obj_delete_confirm_form.html'




class TaskTypesView(LoginRequiredMixin, ListView):
    model = TaskType
    template_name = 'simple_obj/simple_obj_list.html'



class TaskTypeCreate(LoginRequiredMixin, CreateView):
    model = TaskType
    fields = ['title']
    template_name = 'simple_obj/simple_obj_create_form.html'
    success_url = reverse_lazy('task_types_list')



class TaskTypeUpdate(LoginRequiredMixin, UpdateView):
    model = TaskType
    fields = ['title']
    template_name = 'simple_obj/simple_obj_update_form.html'
    success_url = reverse_lazy('task_types_list')



class TaskTypeDelete(LoginRequiredMixin, DeleteView):
    model = TaskType
    success_url = reverse_lazy('task_types_list')
    template_name = 'simple_obj/simple_obj_delete_confirm_form.html'




class TaskStateView(LoginRequiredMixin, ListView):
    model = TaskState
    template_name = 'simple_obj/simple_obj_list.html'



class TaskStateCreate(LoginRequiredMixin, CreateView):
    model = TaskState
    fields = ['title']
    template_name = 'simple_obj/simple_obj_create_form.html'
    success_url = reverse_lazy('task_states_list')



class TaskStateUpdate(LoginRequiredMixin, UpdateView):
    model = TaskState
    fields = ['title']
    template_name = 'simple_obj/simple_obj_update_form.html'
    success_url = reverse_lazy('task_states_list')



class TaskStateDelete(LoginRequiredMixin, DeleteView):
    model = TaskState
    success_url = reverse_lazy('task_states_list')
    template_name = 'simple_obj/simple_obj_delete_confirm_form.html'


def RouteLogedUser()