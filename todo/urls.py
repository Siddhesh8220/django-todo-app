from django.urls import path

from  . import views

urlpatterns = [
path('', views.home, name="home"),
path('todos/', views.index, name="index"),
path('todos/create', views.store, name="store"),
path('todos/<str:todoId>/get', views.show, name="show"),
path('todos/<str:todoId>/edit', views.update, name="update"),
path('todos/<str:todoId>/delete', views.delete, name="delete")
]

