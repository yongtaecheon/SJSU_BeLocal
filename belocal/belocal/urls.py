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
    path('', belocal_app.views.cover, name='main'),
    path('reward_ask/', belocal_app.views.reward_ask, name='reward_ask'),
    path('question1/', belocal_app.views.question1, name='question1'),
    path('question2/', belocal_app.views.question2, name='question2'),
    path('reward_done/', belocal_app.views.reward_done, name='reward_done'),
    path('main/home/', belocal_app.views.main_home, name="main_home"),
    path('guide/home/',belocal_app.views.guide_home, name="guide_home"),
    path('main/wallet/', belocal_app.views.main_wallet, name="main_wallet"),
    path('main/map/', belocal_app.views.main_map, name="main_map"),
    path('main/chat/', belocal_app.views.main_chat, name="main_chat"),
]
