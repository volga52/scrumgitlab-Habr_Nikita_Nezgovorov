from django.db import models


class ArticleCategory(models.Model):
    """Article category model"""

    name = models.CharField(max_length=64, unique=True, verbose_name='название категории')

    class Meta:
        verbose_name = 'Категория Статьи'
        verbose_name_plural = 'Категории Статей'

    def __str__(self):
        return self.name


class Article(models.Model):
    """Article model"""

    title = models.CharField(max_length=512, blank=False, verbose_name='название статьи')
    text = models.TextField(blank=False, verbose_name='содержание статьи')
    create_date = models.DateField(blank=True, auto_now_add=True, verbose_name='дата создания')
    update_date = models.DateField(blank=True, auto_now=True, verbose_name='дата изменения')
    category = models.ForeignKey(ArticleCategory, on_delete=models.PROTECT, verbose_name='название категории')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
