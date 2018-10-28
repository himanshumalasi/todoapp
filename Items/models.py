from django.db import models

# Create your models here.

class TodoList(models.Model):
    name = models.CharField(max_length=180)
    completed = models.BooleanField(default=False)