from rest_framework import serializers 
from .models import Blog 

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=['id','title','body'] 

    def validate(self,data):
        if len(data.get('title'))>8:
            raise serializers.ValidationError("Title is too long, can't exceed 8 characters.")
        return data
