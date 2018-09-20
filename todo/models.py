from django.db import models

# Create your models here.

class Todo(models.Model):
    todo_body = models.CharField(max_length=200)
