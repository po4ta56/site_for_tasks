from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    
    path('types/', TaskTypesView.as_view(), name='task_types_list'),
    path('types/add/', TaskTypeCreate.as_view(), name='task_type_add'),
    path('types/<pk>/', TaskTypeUpdate.as_view(), name='task_type_update'),
    path('types/<pk>/delete/', TaskTypeDelete.as_view(), name='task_type_delete'),
    

    path('states/', TaskStateView.as_view(), name='task_states_list'),
    path('states/add/', TaskStateCreate.as_view(), name='task_states_add'),
    path('states/<pk>/', TaskStateUpdate.as_view(), name='task_states_update'),
    path('states/<pk>/delete/', TaskStateDelete.as_view(), name='task_states_delete'),

    path('', TasksView.as_view(), name='task_list'),
    path('accepted/', TasksAcceptedView.as_view(), name='task_accepted'),
    path('add/', TaskCreate.as_view(), name='task_add'),
    path('free/', TasksFreeView.as_view(), name='task_free'),
    path('performer/', TaskPerformerInterface, name='performer'),
    path('<pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('<pk>/delete/', TaskDelete.as_view(), name='task_delete'),
    path('<pk>/update/', TaskUpdate.as_view(), name='task_update'),
    path('<pk>/accept/', TaskAccept, name='task_accept'),
    path('<pk>/setstate/', TaskSetState.as_view(), name='task_set_state'),
    path('<task_id>/comment/add/', CommentCreateView.as_view(), name='task_detail'),
    
]