from django.db import models

# Create your models here.
class todo_table(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    done = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    
