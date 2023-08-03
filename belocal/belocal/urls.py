"""
URL configuration for belocal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
import belocal_app.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', belocal_app.views.cover),
    path('init/', belocal_app.views.init),
    path('login_personal/',belocal_app.views.login_personal),
    path('signin/',belocal_app.views.signin),
    path('signup/',belocal_app.views.signup),
    path('profile/',belocal_app.views.profile),
    path('register_course/',belocal_app.views.register_course)
]
