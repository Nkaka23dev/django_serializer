from rest_framework import serializers
from .models import Posts

class P_serializer(serializers.ModelSerializer):
    class Meta:
        model=Posts
        fields='__all__'

    def create(self,validated_data):
        return Posts.objects.create(**validated_data)

    def update(self,instance,validate_data):
        instance.title=validate_data.get('title',instance.title)
        instance.content=validate_data.get('content',instance.content)
        instance.save()
        return instance
    
class Student:
    def __init__(self,name,email):
        self.name=name
        self.email=email

def valididate_short(value):
    if len(value)<3:
        raise serializers.ValidationError("Name should not be too short.")
    return value

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100,validators=[valididate_short])
    email=serializers.CharField(max_length=150)

    def validate_name(self,value):
        if len(value)>7:
            raise serializers.ValidationError("Name should be less than 5 characters.")
        return value

    def validate(self,data):
        if data.get('name').startswith('#') or data.get('email').startswith('#'):
            raise serializers.ValidationError("# at start not allowed.")
        return data
    



