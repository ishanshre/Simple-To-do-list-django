from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy
# Create your views here.

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todoapp/tasklist.html'

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todoapp/task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    context_object_name = 'tasks'
    template_name = 'todoapp/task_create.html'

class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name='todoapp/task_update.html'

class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todoapp/task_delete.html'
    success_url = reverse_lazy('todoapp:tasklist')




