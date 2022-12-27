from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, StringRelatedField
from .models import Authors, Book, Biographies


class AuthorsModelSerializer(ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'


class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BiographiesModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biographies

        fields = '__all__'
