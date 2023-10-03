from django.db import models
from django.contrib.auth.models import User
class TODO(models.Model):
    status_choices = [
        ('P', 'Pending'),
        ('C', 'Completed'),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    status= models.CharField(max_length=2,choices=status_choices,default="Pending")
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)