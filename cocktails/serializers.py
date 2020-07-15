from rest_framework import serializers
from .models import *
from accounts.serializers import UserDetailSerializer

class StringListField(serializers.ListField): 
    child = serializers.CharField()

    def to_representation(self, data):
        return ', '.join(data.values_list('name', flat=True))


class Tip_c_Serializer(serializers.HyperlinkedModelSerializer):
    tips = serializers.StringRelatedField(many=True)
    class Meta:
        model = Tip_category
        fields = ('url', 'id', 'name', 'tips')


class Tip_Serializer(serializers.HyperlinkedModelSerializer):
    author = UserDetailSerializer(read_only=True)
    class Meta:
        model = Tip
        fields = ('url', 'id', 'author', 'category', 'title', 'body', 'photo_field', 'pub_date')


class Category_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'id', 'name')


class Ingridient_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingridient
        fields = ('url', 'id', 'name', 'photo_field', 'measurement', 'ing_type')


class Cocktail_Serializer(serializers.HyperlinkedModelSerializer):
    author = UserDetailSerializer()
    tags = StringListField()
    comments = serializers.StringRelatedField(many=True)
    likes = serializers.StringRelatedField(many=True)


    class Meta:
        model = Cocktail
        fields= ('url', 'id', 'author', 'category', 'title', 'photo_field', 'body', 'method', 'pub_date', 'updated_at',  'ingridient', 'tags', 'comments', 'likes')

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        instance = super(MyModelSerializer, self).create(validated_data)
        instance.tags.set(*tags)
        return instance

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags')
        instance = super(MyModelSerializer, self).create(validated_data)
        instance.tags.set(*tags)
        return instance


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class Comment_Serializer(serializers.HyperlinkedModelSerializer):
    reply_set = RecursiveSerializer(many=True, read_only=True)
    author = UserDetailSerializer()
    class Meta:
        model = Comment
        fields = ('url', 'id', 'author', 'body', 'cocktail', 'date', 'parent', 'reply_set')


class Like_Serializer(serializers.HyperlinkedModelSerializer):
    user = UserDetailSerializer(), 
    class Meta:
        model = Like
        fields = ('url', 'id', 'user', 'value', 'cocktail')