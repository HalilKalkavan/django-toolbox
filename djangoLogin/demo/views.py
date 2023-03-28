# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
# from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
# class Another(View):
#     books = Book.objects.all()
#
#     title = ''
#     for book in books:
#         title += f"Book title {book.title}, and book description {book.description}<br>"
#
#     def get(self, request):
#         return HttpResponse(self.title)
#
#
# def first(request):
#     return HttpResponse('First Message')