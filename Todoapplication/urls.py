"""Todoapplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views import View
from myapp import views
from rest_framework.routers import DefaultRouter
from todoapi import views
router=DefaultRouter()
router.register("todos",views.TodosView,basename="todos")


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path("todos/add",views.TodoCreateView.as_view(),name="todo-add"),
    # path("todos/all",views.TodoListView.as_view(),name="todo-list"),
    # path("todos/detail/<int:id>",views.TodoDetailView.as_view(),name="todo-detail"),
    # path("todos/remove/<int:id>",views.TodoDeleteView.as_view(),name="todo-delete"),
    # path("todos/change/<int:id>",views.TodoEditView.as_view(),name="todo-change"),
    # path("register",views.RegistraionView.as_view(),name="register"),
    # path("",views.LoginView.as_view(),name="signin"),
    # path("logout",views.signout,name="signout")
]+router.urls
