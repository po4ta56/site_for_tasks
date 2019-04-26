from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import *
from .forms import *



class TasksView(LoginRequiredMixin, ListView):  
    model = Task
    template_name = 'tasks_list.html'
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Task.objects.all().for_customer(self.request.user)



class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'task_type', 'description']
    template_name = 'simple_obj/simple_obj_create_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'task_type', 'description']
    template_name = 'simple_obj/simple_obj_update_form.html'
    success_url = reverse_lazy('task_list')

    def get_object(self, queryset=None):
        user = self.request.user
        if self.request.user.is_authenticated:
            obj = super(TaskUpdate, self).get_object(queryset)
            if obj:
                if obj.author == user:
                    return obj
        return HttpResponse(status=404)



class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    template_name = 'simple_obj/simple_obj_delete_confirm_form.html'


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "task_detail.html"



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
    template_name = 'simple_obj/simple_obj_delete_confirm_form.html'
    success_url = reverse_lazy('task_states_list')






class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['firstname', 'lastname', 'profile__customer']
    template_name = 'simple_obj/simple_obj_update_form.html'
    success_url = reverse_lazy('route')


@login_required
def RouteLogedUserView(request):
    user = request.user
    if user.is_authenticated:
        if user.profile.customer:
            return redirect('task_list')
        else:
            return redirect('task_list')
    return redirect('login')


class CreateUserView(CreateView):
    models = User
    fields = ['firstname', 'lastname', 'email', 'login', 'password']
    template_name = 'simple_obj/simple_obj_create_form.html'
    success_url = reverse_lazy('profile')

    def get_form_class(self):
        return UserCreationForm