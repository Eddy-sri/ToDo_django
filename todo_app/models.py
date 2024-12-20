from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField()
    created_date = models.DateTimeField()

    def __str__(self):
        
        return self.title