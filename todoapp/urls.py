from django.urls import path
from .views import TaskList, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
app_name = 'todoapp'
urlpatterns = [
    path('',TaskList.as_view(),name= 'tasklist'),
    path('task_detail/<int:pk>/', TaskDetailView.as_view(), name='taskdetail'),
    path('task_create/',TaskCreateView.as_view(),name='taskcreate'),
    path('task_detail/<int:pk>/update/', TaskUpdateView.as_view(),name='taskupdate'),
    path('task_detail/<int:pk>/delete/', TaskDeleteView.as_view(),name='taskdelete'),
]
