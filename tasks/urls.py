from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', TasksView.as_view()),
    #path('tasks/', TasksView.as_view()),
    path('types/', TaskTypeView.as_view(), name='task_types_list'),
    path('types/add', TaskTypeCreate.as_view(), name='task_type_add'),
    path('types/<pk>/', TaskTypeUpdate.as_view(), name='task_type_update'),
    path('types/<pk>/delete/', TaskTypeDelete.as_view(), name='task_type_delete')
]