from django.shortcuts import render
from elasticsearch import Elasticsearch, RequestsHttpConnection
from rest_framework_elasticsearch import es_views, es_pagination, es_filters
from .search_indexes import CocktailIndex


CocktailIndex.init(using=es_client)

class CocktailView(es_views.ListElasticAPIView):
    es_client = Elasticsearch(hosts=['elasticsearch:9200/'],
                              connection_class=RequestsHttpConnection)


    es_pagination_class = es_pagination.ElasticLimitOffsetPagination

    es_model = CocktailIndex

    es_filter_backends = (
        es_filters.ElasticFieldsFilter,
        es_filters.ElasticSearchFilter,
        es_filters.ElasticOrderingFilter,
    )

    es_ordering_fields = (
        "pub_date",
        ("title.raw", "title")
    )

    es_filter_fields = (
        es_filters.ESFieldFilter('tag', 'tags'),
    )
    es_search_fields = (
        'tags',
        'title',
    )
