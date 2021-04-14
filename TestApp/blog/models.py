from django.db import models

class User(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    desc=models.TextField()

    def __str__(self):
        return self.email
