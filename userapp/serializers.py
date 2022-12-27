from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, StringRelatedField
from django.contrib.auth.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'last_name']


class UserFullModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



