"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    TitleViewSet,
    GenreViewSet,
    ReviewsViewSet,
    CommentsViewSet
)

router1 = DefaultRouter()

router1.register('category', CategoryViewSet, basename='category')
router1.register('title', TitleViewSet, basename='title')
router1.register('genre', GenreViewSet, basename='genre')
router1.register(
    r'title/(?P<title_id>\d+)/review',
    ReviewsViewSet,
    basename='review'
),
router1.register(
    r'title/(?P<title_id>\d+)/review/(?P<review_id>\d+)/comment',
    CommentsViewSet,
    basename='comment'
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('api.urls')),
    path('v1/api/', include(router1.urls)),
]
