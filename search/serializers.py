from __future__ import (absolute_import, division, print_function, unicode_literals)
from rest_framework_elasticsearch.es_serializer import ElasticModelSerializer

from cocktails.models import Cocktail
from accounts.models import User
from .documents import CocktailIndex



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username')


class ElasticCocktailSerializer(ElasticModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Cocktail
        es_model = CocktailIndex
        fields = ('pk', 'title', 'pub_date', 'tags', 'body', 'updated_at', 'author')