"""site_for_tasks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from tasks.views import ProfileUpdateView, RouteLogedUserView, CreateUserView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='route', permanent=False)),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<pk>/', ProfileUpdateView.as_view(), name='profile'),
    path('passreset/', PasswordResetView.as_view(), name='pass_reset'),
    path('registration/', CreateUserView.as_view(), name='registration'),
    path('route/', RouteLogedUserView, name="route"),
    path('tasks/', include('tasks.urls'))
]
