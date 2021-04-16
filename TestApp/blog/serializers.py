from django.contrib.auth.models import User
from  rest_framework import serializers

class Userserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=['url','id','username','email','password']
        extra_kwargs={'password':{'write_only':True,'required':True}}

    def create(self,validated_data):
        user=User.objects.create(**validated_data)
        return user