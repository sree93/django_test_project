from rest_framework import generics

from bookstore.models import Book
from bookstore.serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()


class BooksOfAuthorListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(author=self.kwargs['author_id'])
