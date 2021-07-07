from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=120)
    body=models.TextField(default='')

    def __str__(self):
        return self.title
