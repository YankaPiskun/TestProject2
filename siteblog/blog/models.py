from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название категории')
    slug = models.SlugField(max_length=150, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название тэга')
    slug = models.SlugField(max_length=150, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название поста')
    slug = models.SlugField(max_length=150, verbose_name='Url', unique=True)
    author = models.CharField(max_length=150, verbose_name='Автор')
    content = models.TextField(max_length=250, blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликованно')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Тэг')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']
# Create your models here.
