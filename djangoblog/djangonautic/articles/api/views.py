from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.models import User

from ..models import Article
from .serializers import ArticleSerializer


@permission_classes((IsAuthenticated,))
class ArticleAPIView(APIView):

    def get(self, request, id=None):
        if id is not None:
            article    = Article.objects.get(id=id)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        articles   = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        author     = User.objects.get(id=request.user.id)
        article    = Article(author=author)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            article = Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if article.author != request.user:
            return Response({'Permission Denied': 'You cannot update this article!'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ArticleSerializer(article, request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            article = Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if article.author != request.user:
            return Response({'Permission Denied': 'You cannot delete this article!'}, status=status.HTTP_400_BAD_REQUEST)

        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticlesPaginationView(generics.ListAPIView):
    queryset               = Article.objects.all()
    serializer_class       = ArticleSerializer
    pagination_class       = PageNumberPagination
    permission_classes     = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    filter_backends        = (SearchFilter, OrderingFilter)
    search_fields          = ('title', 'body', 'thumb', 'author__username')