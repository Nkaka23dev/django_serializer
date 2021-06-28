from rest_framework import serializers  
from .models import BlogModel

class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogModel 
        fields=['user','title','content'] 

    def create(self,validated_data):
        return BlogModel.objects.create(**validated_data) 

    def update(self,instance,validated_data):
        instance.user=validated_data.get('user',instance.user)
        instance.title=validated_data.get('title',instance.title)
        instance.content=validated_data.get('content',instance.content)
        instance.save()
        return instance

class Person:
    def __init__(self,first_name,last_name):
        self.first_name=first_name 
        self.last_name=last_name 

def no_more_than_2_char(value):
    if len(value)>2:
        raise serializers.ValidationError("Characters can't be more than 2.")
    return value

class PersonSerializer(serializers.Serializer):
    first_name=serializers.CharField(max_length=300,validators=[no_more_than_2_char]) 
    last_name=serializers.CharField(max_length=300) 

    def validate_first_name(self,value):
        if len(value)>5:
            raise serializers.ValidationError("First name can not be more than 5 characters.")
        return value

    def validate(self,data):
        if data.get('first_name').startswith('#') or data.get('last_name').startswith('#'):
            raise serializers.ValidationError("Last Name can not start with a #")
        return data 




