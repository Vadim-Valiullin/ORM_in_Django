from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.name


class User(models.Model):
    ROLES = [('member', 'Пользователь'), ('moderator', 'Модератор'), ('admin', 'Админ')]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLES, default='member')
    # author_id = models.CharField()
    age = models.PositiveIntegerField()
    locations = models.ManyToManyField(Location)

    class Meta:

        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username


class Ads(models.Model):
    name = models.CharField(max_length=100)
    # author = models.CharField(max_length=100, null=True)
    author = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1500, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='aaa/image/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    class Meta:

        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name