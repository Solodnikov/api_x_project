from django.db import models

# Create your models here.


class Categories(models.Model):
    """Типы произведений"""
    name = models.CharField(
        max_length=100,
        verbose_name='Название категории произведений'
    )
    slug = models.SlugField(
        max_length=100,
        allow_unicode=True,
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




# Genres
# Titles
# Reviews
# Comments
# Users


