from rest_framework import serializers 
from .models import Post  

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post 
        fields='__all__'  
    
    def create(self,validated_data):
        return Post.objects.create(**validated_data) 

    def update(self,instance,validate_data):
        instance.title=validate_data.get('title',instance.title)
        instance.content=validate_data.get('content',instance.content) 
        instance.save()
        return instance

    def validate(self,data):
        if len(data.get('title'))>4:
            raise serializers.ValidationError("Title must be less than 2 chars") 
        return data
        

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname  

def no_more_than_2_char(value):
    if len(value)>2:
        raise serializers.ValidationError("Chars are exceeding Two.")
    return value
        
class PersonSerializer(serializers.Serializer):
    fname=serializers.CharField(max_length=100,validators=[no_more_than_2_char]) 
    lname=serializers.CharField(max_length=100) 

    def validate_fname(self,value):
        if len(value)>5:
            raise serializers.ValidationError("User name shouldn't be more than 5 characters.")
        return value 

    def validate(self,data):
        if data.get('fname').startswith('#') or data.get('lname').startswith('#'):
            raise serializers.ValidationError("Name should not start with a #")
        return data

    
     

