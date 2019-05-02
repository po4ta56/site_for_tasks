from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.db import transaction
from .models import *
from .forms import *



class TasksView(LoginRequiredMixin, ListView):  
    model = Task
    template_name = 'tasks_list.html'
    redirect_field_name = 'redirect_to'

    def dispatch(self, request, *args, **kwargs):
        self.filter_form = TaskFilterForm(request.GET)
        self.filter_form.is_valid()
                    
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.filter_form
        return context

    def get_queryset(self):
        if self.filter_form.cleaned_data['task_type']:
            queryset = Task.objects.all(). \
                for_customer(self.request.user). \
                filter(task_type=self.filter_form.cleaned_data['task_type'])
        else:
            queryset = Task.objects.all().for_customer(self.request.user)

        queryset = queryset.select_related(
            'task_type', 'state', 'author'
        )

        return queryset



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


class TaskSetState(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['state']
    template_name = 'simple_obj/simple_obj_update_form.html'
    success_url = reverse_lazy('task_list')



class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    template_name = 'simple_obj/simple_obj_delete_confirm_form.html'


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks_detail.html"



class TasksAcceptedView(LoginRequiredMixin, ListView):  
    model = Task
    template_name = 'tasks_list.html'
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Task.objects.all().for_performer(self.request.user)



class TasksFreeView(LoginRequiredMixin, ListView):  
    model = Task
    template_name = 'tasks_list.html'
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Task.objects.all().for_free()


@login_required
@transaction.atomic
def TaskAccept(request, pk):
    task = get_object_or_404(Task, id=pk)
    if task.performers.all().count()==0:
        task.performers.add(request.user)
        task.save()
        return HttpResponse('Задача принята вами!')
    return HttpResponse('Неудача!')
    #return redirect(task.get_url())



def TaskPerformerInterface(request):
    return render(request, 'tasks_performer_interface.html')


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
    model = Profile
    fields = ['customer']
    template_name = 'simple_obj/simple_obj_update_form.html'
    success_url = reverse_lazy('route')



@login_required
def RouteLogedUserView(request):
    user = request.user
    if user.is_authenticated:
        if user.profile.customer:
            return redirect('task_list')
        else:
            return redirect('performer')
    return redirect('login')


class CreateUserView(CreateView):
    models = User
    fields = ['firstname', 'lastname', 'email', 'login', 'password']
    template_name = 'simple_obj/simple_obj_create_form.html'
    
    def get_form_class(self):
        return UserCreationForm

    def get_success_url(self):
        return reverse_lazy('profile', args=[self.object.pk])
        


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['description']
    template_name = 'simple_obj/simple_obj_create_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        tasksSet = get_object_or_404(Task, id=self.kwargs['task_id'])
        if tasksSet:
            form.instance.task = tasksSet
            self.success_url = form.instance.task.get_url()
        return super().form_valid(form)



