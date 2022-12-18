# import base64
# from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from base.models import Categories, Genres, Titles, Reviews, Comments


# class Base64ImageField(serializers.ImageField):
#     def to_internal_value(self, data):
#         if isinstance(data, str) and data.startswith('data:image'):
#             format, imgstr = data.split(';base64,')
#             ext = format.split('/')[-1]
#             data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
#         return super().to_internal_value(data)

class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Categories


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Genres


class TitlesSerializer(serializers.ModelSerializer):
    genre=serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genres.objects.all()
    )
    category=serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Titles


class ReviewsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Reviews
        read_only_fields = ('title',)


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Comments
        read_only_fields = ('title', 'review')
