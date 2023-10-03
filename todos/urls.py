from django.urls import path
from . import views

urlpatterns = [
    
    path('todo/', views.home_view, name='todos'),
    path('add-todo/', views.add_view, name='add-todo'),
    path('edit-todo/<int:todo_id>/', views.edit_view, name='edit-todo'),
    path('delete-todo/<int:todo_id>/', views.delete_view, name='delete-todo'),

]