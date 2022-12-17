from django.db import models


class Categories(models.Model):
    """Типы произведений"""
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название категории произведений'
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='Адрес страницы категории произведений'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        constraints = [
            models.UniqueConstraint(
                name="%(app_label)s_%(class)s_unique_relationships",
                fields=["name", "slug"],
            ),
        ]

    def __str__(self) -> str:
        return self.name[:30]


class Genres(models.Model):
    """Жанры произведений"""
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Наименование жанра произведения'
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='Адрес страницы жанра произведения'
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        constraints = [
            models.UniqueConstraint(
                name="%(app_label)s_%(class)s_unique_relationships",
                fields=["name", "slug"],
            ),
        ]

    def __str__(self) -> str:
        return self.name[:30]


class Titles(models.Model):
    """Название произведения"""
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование произведения'
    )
    year = models.IntegerField(
        # min_value=1000,
        # max_value=2022,
        verbose_name='Год произведения'
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    genre = models.ForeignKey(
        Genres,
        related_name='titles',
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Categories,
        related_name='titles',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        constraints = [
            models.UniqueConstraint(
                name="%(app_label)s_%(class)s_unique_relationships",
                fields=["name", "year", "description", "genre", "category"],
            ),
        ]


class Reviews(models.Model):
    """Название произведения"""
    title = models.ForeignKey(
        Titles,
        related_name='review',
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name='Отзыв'
    )
    score = models.IntegerField(
        verbose_name='Балы'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


# Comments
# Users
