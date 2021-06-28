from django.db import models

class BlogModel(models.Model):
    user=models.CharField(max_length=400)
    title=models.CharField(max_length=200)
    content=models.TextField(default='')

    def __str__(self):
        return self.title