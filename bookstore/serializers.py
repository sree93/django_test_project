# book ={
#     name: 'sadas',
#     author: 'name'
# }
#
#
# author = {
#       id:dada
#     name:'asdasd',
#     age: 12,
#     gender: 'male'
# }
#
#
# book {
#     name: 'asdasdas',
#     author: {
#     name:'asdasd',
#     age: 12,
#     gender: 'male'
# }
# }
from rest_framework import serializers

from bookstore.models.author import Author
from bookstore.models.book import Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = [
            'gender'
        ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = []
