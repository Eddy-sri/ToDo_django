from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField()
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        
        return self.title