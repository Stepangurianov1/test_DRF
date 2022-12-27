from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .serializers import UserModelSerializer
from .serializers import UserFullModelSerializer


# Create your views here.
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserFullModelSerializer
        return UserModelSerializer
