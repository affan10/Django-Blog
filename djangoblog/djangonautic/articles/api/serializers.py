from rest_framework import serializers
from ..models import Article


class ArticleSerializer(serializers.ModelSerializer):

    author_name = serializers.SerializerMethodField('get_author')
    class Meta:
        model  = Article
        fields = ('id', 'title', 'slug', 'body', 'date', 'thumb', 'author_name')

    def get_author(self, Article):
        return Article.author.username