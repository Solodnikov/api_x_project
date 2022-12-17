from rest_framework import viewsets, mixins, filters, permissions
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination

from base.models import Categories, Titles, Genres, Reviews
# from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CategoriesSerializer, TitlesSerializer, GenresSerializer, ReviewsSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    # permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    # permission_classes = (IsAuthorOrReadOnly,)
    # pagination_class = LimitOffsetPagination


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    # permission_classes = (IsAuthorOrReadOnly,)
    # pagination_class = LimitOffsetPagination


class ReviewsViewSet(viewsets.ModelViewSet):
    # queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

    def get_title(self):
        title_id = self.kwargs.get('title_id')
        return get_object_or_404(Titles, pk=title_id)

    def get_queryset(self):
        return self.get_title().review.all()

    def perform_create(self, serializer):
        serializer.save(title=self.get_title())


# class CommentViewSet(viewsets.ModelViewSet):
#     serializer_class = CommentSerializer
#     permission_classes = (IsAuthorOrReadOnly,)

#     def get_post(self):
#         post_id = self.kwargs.get('post_id')
#         return get_object_or_404(Post, pk=post_id)

#     def get_queryset(self):
#         return self.get_post().comments.all()

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user, post=self.get_post())


# class FollowViewSet(
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     viewsets.GenericViewSet
# ):
#     serializer_class = FollowSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#     filter_backends = (filters.SearchFilter, )
#     search_fields = ('following__username',)

#     def get_queryset(self):
#         return self.request.user.follower.all()

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
