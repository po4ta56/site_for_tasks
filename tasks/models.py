from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class TaskState(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Статус задачи'
        verbose_name_plural = 'Статусы задачи'


class TaskType(models.Model):
    title = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Тип задачи'
        verbose_name_plural = 'Типы задачи'


class Task(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=500)
    state = models.ForeignKey(TaskState, on_delete=models.PROTECT)
    task_type = models.ForeignKey(TaskType, on_delete=models.PROTECT)
    performers = models.ManyToManyField(User)

    class Meta:
        ordering = ['date', 'title']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Comment(models.Model):
    date = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=500)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    
