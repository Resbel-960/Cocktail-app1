from __future__ import (absolute_import, division, print_function, unicode_literals)

from elasticsearch_dsl import (
    Document,
    Date,
    Keyword,
    Text,
    Boolean,
    Integer
)

class CocktailIndex(Document):

    pk = Integer()
    # author = Object(
    #     properties={
    #         'username': Text(fields={'raw': Keyword()}),
    #         'pk': Integer(),
    #     }
    # )
    title = Text(fields={'raw': Keyword()})
    pub_date = Date()
    updated_at = Date()
    body=Text()
    tags = Keyword(multi=True)

    class Meta:
        index = 'cocktail'

