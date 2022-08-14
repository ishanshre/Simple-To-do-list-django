from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']
    
    def get_absolute_url(self):
        return reverse('todoapp:taskdetail', kwargs={'pk':self.pk})
        