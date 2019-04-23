from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


class Profile(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer = models.BooleanField(verbose_name='Заказчик', default=False)

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
    title = models.CharField(verbose_name='Наименование', max_length=100, unique=True)

    def __str__(self):      
        return "{{ {0} : {1} }}".format(self._meta.verbose_name, self.title)

    class Meta:
        verbose_name = 'Статус задачи'
        verbose_name_plural = 'Статусы задачи'


class TaskType(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=100, unique=True)
    
    def __str__(self):      
        return "{{ {0} : {1} }}".format(self._meta.verbose_name, self.title)

    class Meta:
        verbose_name = 'Тип задачи'
        verbose_name_plural = 'Типы задачи'


class Task(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=150)
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    description = models.TextField(verbose_name='Описание', max_length=500)
    state = models.ForeignKey(TaskState, on_delete=models.PROTECT)
    task_type = models.ForeignKey(TaskType, on_delete=models.PROTECT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_task_auth')
    performers = models.ManyToManyField(User, related_name='user_task_performers')

    def __str__(self):      
        return "{{ {0} : {1} }}".format(self._meta.verbose_name, self.title)

    class Meta:
        ordering = ['date', 'title']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Comment(models.Model):    
    date = models.DateTimeField(verbose_name="Дата", auto_now=True)
    description = models.TextField(verbose_name="Содержание", max_length=500)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):      
        return "{{ {0} : {1} {2} }}".format(self._meta.verbose_name, self.date, self.author)

    class Meta:
        ordering = ['date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    
