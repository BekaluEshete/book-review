from flask import Response
from rest_framework import viewsets
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated




def root_view(request):
    return JsonResponse({'message': 'Welcome to the Book API'})

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
