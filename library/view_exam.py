from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from authors.models import Book

from authors.serializers import BookModelSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet


class BookAPIVIew(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, format=None):
        book = Book.objects.all()
        serializer = BookModelSerializer(book, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        pass


from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    get_object_or_404


class BookCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


# class BookListAPIView(ListAPIView):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer


class BookRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BookUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BookDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


from rest_framework import viewsets


class BookViewSet(ViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def list(self, request):
        books = Book.objects.all()
        serializer = BookModelSerializer(books, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def only(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        return Response({'book.name': book.name})

    def retrieve(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookModelSerializer(book)
        return Response(serializer.data)


# class BookModelViewSet(ModelViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer
#
#     def get_queryset(self):
#         return Book.objects.filter(name__contains='boo')# по совпадению как регулярка


class BookListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = BookModelSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Book.objects.filter(name__contains=name)


class BookCustomerViewSet(ListModelMixin, DestroyModelMixin, GenericViewSet, RetrieveModelMixin):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BookModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        book = Book.objects.all()
        if name:
            book = Book.objects.filter(name__contains='boo')
        return book  # по совпадению как


class FilterBook(ModelViewSet):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()
    filterset_fields = ['id', 'name']
