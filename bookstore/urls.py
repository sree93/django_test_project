from django.urls import path

from bookstore.views.author import AuthorListCreateAPIView, AuthorRetrieveUpdateDestroyAPIView
from bookstore.views.book import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView, BooksOfAuthorListAPIView

urlpatterns = [
    path('author/', AuthorListCreateAPIView.as_view()),
    path('author/<int:pk>/', AuthorRetrieveUpdateDestroyAPIView.as_view()),
    path('book/', BookListCreateAPIView.as_view()),
    path('book/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),
    path('book/author/<int:author_id>/', BooksOfAuthorListAPIView.as_view()),
]


