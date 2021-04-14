from django.db import models
from datetime import datetime

class Posts(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    posted_date=models.DateField(("Date"), auto_now_add=True)
    
    def __str__(self):
        return self.content