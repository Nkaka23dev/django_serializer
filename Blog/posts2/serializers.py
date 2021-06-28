from rest_framework import serializers 
from .models import BlogModel2 

class BlogModel2serializer(serializers.ModelSerializer):
    class Meta:
        model=BlogModel2 
        fields='__all__'