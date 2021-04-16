from rest_framework import serializers
from .models import Posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Posts
        fields=['id','title','content','posted_date']

    def create(self,validated_data):
        return Posts.objects.create(**validated_data)   

    def update(self,instance,validate_data):
        instance.title=validate_data.get('title',instance.title)
        instance.content=validate_data.get('title',instance.title)
        instance.save()
        return instance

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

def not_less_than_2(value):
    if len(value)<3:
        raise serializers.ValidationError("User name should not be less than 3 characters")
    return value

class PersonSerializer(serializers.Serializer):
    fname=serializers.CharField(max_length=100,validators=[not_less_than_2])
    lname=serializers.CharField(max_length=150)

    def validate_fname(self,value):
        if len(value)>6:
            raise serializers.ValidationError("User name should not be greater than 6 characters")
        return value

    def validate(self,data):
        if data.get('fname').startswith('#') or data.get('lname').startswith('#'):
            raise serializers.ValidationError("Name should not start with #.")
        return data

