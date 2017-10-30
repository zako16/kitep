from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Years(models.Model):
    class Meta:
        verbose_name = 'Год выхода книги'
        verbose_name_plural = 'Года'
    year = models.IntegerField(null=False)

    def __str__(self):
        return str(self.year)


class Statuses(models.Model):
    class Meta:
        verbose_name = 'Статус(Состояние) книги'
        verbose_name_plural = 'Статусы книг'
    status = models.CharField(null=False, max_length=255)

    def __str__(self):
        return self.status


class CoverTypes(models.Model):
    class Meta:
        verbose_name = 'Тип обложки'
        verbose_name_plural = 'Типы обложек'
    type = models.CharField(null=False, max_length=255)

    def __str__(self):
        return self.type


class Publisher(models.Model):
    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'
    title = models.CharField(null=False, max_length=255)

    def __str__(self):
        return self.title


class Books(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50, null=True)
    cover = models.ImageField(null=True, upload_to='books/covers')
    category = models.ForeignKey(Categories)
    description = models.TextField()
    user = models.ForeignKey(User)
    year = models.ForeignKey(Years, null=True)
    coverType = models.ForeignKey(CoverTypes, null=True)
    publisher = models.ForeignKey(Publisher, null=True)
    status = models.ForeignKey(Statuses, null=True)
    # цена или обмен
    exchange = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Закрыто ли предложение или нет
    is_issue = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_price(self):
        return self.price if self.sale else None
