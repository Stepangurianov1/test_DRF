import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from django.contrib.auth.models import User
from .views import AuthorModelViewSet, BookModelViewSet
from .models import Authors, Book


class TestAuthorViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors')
        view = AuthorModelViewSet.as_view(actions={'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors',
                               {'first_name': 'Александр', 'last_name': 'Пушкин', 'birthday_year': 2000})
        view = AuthorModelViewSet.as_view(actions={'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors',
                               {'first_name': 'Александр', 'last_name': 'Пушкин', 'birthday_year': 2000})
        admin = User.objects.create_superuser('admin', 'admin@gmail.com', 'admin1')
        force_authenticate(request, admin)
        view = AuthorModelViewSet.as_view(actions={'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        author = Authors.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
        client = APIClient()
        response = client.get(f'/api/authors/{author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_quest(self):
        user = User.objects.create_superuser('admin', 'admin@gmail.com', 'admin1')
        author = Authors.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.put(f'/api/authors/{author.id}/',
                              {'first_name': 'Говард', 'last_name': 'Лавкфарт', 'birthday_year': 1880})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        user = User.objects.create_superuser('admin', 'admin@gmail.com', 'admin1')
        author = Authors.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.put(f'/api/authors/{author.id}/',
                              {'first_name': 'Говард', 'last_name': 'Лавкфарт', 'birthday_year': 1880})
        author = Authors.objects.get(pk=user.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(author.first_name, 'Говард')


class TestMath(APISimpleTestCase):
    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)


class TestBookViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_book(self):
        author = Authors.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
        book = Book.objects.create(name='Людмила')
        book.authors.add(author)
        # book = mixer.blend(Book)
        book.save()
        print(book.authors)
        user = User.objects.create_superuser('admin', 'admin@gmail.com', 'admin1')
        self.client.force_authenticate(user=user)
        response = self.client.put(f'/api/books/{book.id}/', {'name': 'Руслан', 'authors': author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

