from django.db import models

# Create your models here.

class Todo(models.Model):
    id = models.TextField(max_length=500, primary_key=True)
    description = models.TextField(max_length=500)
    iscomplete = models.BooleanField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
