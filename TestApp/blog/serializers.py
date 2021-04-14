from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import User

# class Person:
#    def __init__(self,first_name,last_name):
#       self.first_name=first_name
#       self.last_name=last_name

# def no_more_than_2_char(value):
#    if len(value)<2:
#       raise serializers.ValidationError("Not less than 2 characters.")
#    return value

# class Serializer(serializers.Serializer):
#    first_name=serializers.CharField(max_length=200,validators=[no_more_than_2_char])
#    last_name=serializers.CharField(max_length=200)

#    def validate_first_name(self,value):
#       if len(value)>5:
#          raise serializers.ValidationError("First name should not exceed 5 charcters")
#       return value 

#    def validate(self,data):
#       if data.get("first_name").startswith("#") or data.get("last_name").startswith("#"):
#          raise serializers.ValidationError("Name should not start with #")
#       return data


class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model=User
      fields="__all__"

   def create(self,validated_data):
      return User.objects.create(**validated_data)

   def update(self,instance,validated_data):
      instance.name=validated_data.get('title',instance.name)
      instance.email=validated_data.get('email',instance.email)
      instance.desc=validated_data.get('desc',instance.desc)
      instance.save()
      return instance


