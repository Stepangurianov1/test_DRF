from django.contrib import admin
from django.urls import path, include

from library.view_exam import BookAPIVIew

from library.view_exam import BookCreateAPIView, BookListAPIView, BookUpdateAPIView, BookDestroyAPIView, \
    BookRetrieveAPIView, BookViewSet, BookCustomerViewSet, BookModelViewSet, FilterBook
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('book', BookViewSet, basename='book')
# router.register('book_model', BookModelViewSet)
# router.register('customer_book', BookCustomerViewSet)
router.register('book_f', FilterBook)
urlpatterns = [
    path('api-filter/<str:name>/', BookListAPIView.as_view()),
    path('api-view/', BookAPIVIew.as_view()),
    path('api/create/', BookCreateAPIView.as_view()),
    path('api/list/', BookListAPIView.as_view()),
    path('api/update/<int:pk>/', BookUpdateAPIView.as_view()),
    path('api/delete/<int:pk>/', BookDestroyAPIView.as_view()),
    path('api/detail/<int:pk>/', BookRetrieveAPIView.as_view()),
    path('api/', include(router.urls)),
]