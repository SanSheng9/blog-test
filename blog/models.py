from django.db import models

# USER
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField( max_length=255, unique=True)
    username = models.CharField(primary_key=True, max_length=255, unique=True)
    password = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, default='avatar.png', verbose_name='Аватар')
    about_me = models.CharField(max_length=255, default="I'm new user!", blank=False)


# POST

class Post(models.Model):
    title = models.CharField(max_length=225, verbose_name='Название поста')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, default='default.png', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Логин автора')

    def __str__(self):
        return f'Id {self.id}: {self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['title']

class Comment(models.Model):
    body = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateField(auto_now=True, verbose_name='Опубликовано')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Id {self.id}: {self.post} by {self.author}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['author']