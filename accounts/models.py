from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Person(models.Model):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    avatar = models.ImageField(null=True, upload_to='accounts/avatars/')
    description = models.TextField(null=True)
    phone_number = models.CharField(max_length=255)
    user = models.OneToOneField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class PhoneNumbers(models.Model):
    class Meta:
        verbose_name = 'Контактный номер'
        verbose_name_plural = 'Контактные номера'
    number = models.CharField(max_length=255)
    user = models.ForeignKey(Person)
    #
    # def __str__(self):
    #     return self.user.user.username, self.number