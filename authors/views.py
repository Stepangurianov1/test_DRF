from django.shortcuts import render
from rest_framework.permissions import AllowAny, BasePermission

from .models import Authors, Book, Biographies
from .serializers import AuthorsModelSerializer, BookModelSerializer, BiographiesModelSerializer
from rest_framework.viewsets import ModelViewSet


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class AuthorModelViewSet(ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsModelSerializer


# Create your views here.
class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    # permission_classes = [StaffOnly]


class BiographiesModelViewSet(ModelViewSet):
    queryset = Biographies.objects.all()
    serializer_class = BiographiesModelSerializer
