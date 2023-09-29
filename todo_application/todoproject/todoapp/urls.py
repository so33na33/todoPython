
from django.urls import path, include
from . import views
app_name='todoapp'

urlpatterns = [
    path('',views.demo,name="demo"),
    # path('next/',views.demo1,name="demo1")
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('listview/',views.todoList.as_view(),name="todolist"),
    path('detailView/<int:pk>/',views.todoDetail.as_view(),name="todoDetail"),
    path('updateView/<int:pk>/',views.todoUpdate.as_view(),name="todoUpdate"),
    path('deleteView/<int:pk>/',views.todoDelete.as_view(),name="todoDelete")
]
