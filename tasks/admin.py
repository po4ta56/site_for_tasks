from django.contrib import admin
from tasks.models import Profile, TaskType, TaskState, Task, Comment

'''
admin.site.register(Profile)
admin.site.register(TaskType)
admin.site.register(TaskState)
admin.site.register(Task)
admin.site.register(Comment)
'''

@admin.register(Profile, TaskType, TaskState, Task, Comment)
class AuthorAdmin(admin.ModelAdmin):
    pass