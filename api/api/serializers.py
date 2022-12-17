# import base64
# from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from base.models import Categories, Genres, Titles, Reviews


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


# class PostSerializer(serializers.ModelSerializer):
#     author = serializers.SlugRelatedField(
#         slug_field='username',
#         read_only=True
#     )
#     image = Base64ImageField(required=False, allow_null=True)

#     class Meta:
#         fields = '__all__'
#         model = Post


# class CommentSerializer(serializers.ModelSerializer):
#     author = serializers.SlugRelatedField(
#         slug_field='username',
#         read_only=True
#     )

#     class Meta:
#         fields = '__all__'
#         model = Comment
#         read_only_fields = ('post',)


# class GroupSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Group
#         fields = (
#             "id",
#             "title",
#             "slug",
#             "description",
#         )


# class FollowSerializer(serializers.ModelSerializer):
#     user = serializers.SlugRelatedField(
#         slug_field='username',
#         queryset=User.objects.all(),
#         default=serializers.CurrentUserDefault(),
#     )
#     following = serializers.SlugRelatedField(
#         slug_field='username',
#         queryset=User.objects.all()
#     )

#     class Meta:
#         model = Follow
#         fields = '__all__'
#         read_only_fields = ('user',)
#         validators = (
#             UniqueTogetherValidator(
#                 queryset=Follow.objects.all(),
#                 fields=('user', 'following'),
#                 message=('Подписка на автора оформлена ранее!')
#             ),
#         )

#     def validate_following(self, value):
#         if self.context['request'].user == value:
#             raise serializers.ValidationError(
#                 'Нельзя подписаться на самого себя!')
#         return value
