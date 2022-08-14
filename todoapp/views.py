from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todoapp/tasklist.html'

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todoapp/task_detail.html'

class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    fields = '__all__'
    context_object_name = 'tasks'
    template_name = 'todoapp/task_create.html'

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    fields = '__all__'
    template_name='todoapp/task_update.html'

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todoapp/task_delete.html'
    success_url = reverse_lazy('todoapp:tasklist')




