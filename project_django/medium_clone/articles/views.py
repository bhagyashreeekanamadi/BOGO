from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Article
from .serializers import ArticleSerializer
# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

