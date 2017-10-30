from django.db import models

# Create your models here.


class News(models.Model):
    """docstring for News"""
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    title = models.CharField(max_length=45)
    description = models.TextField()
    image = models.ImageField(upload_to='news/images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
