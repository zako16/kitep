from django.db import models

# Create your models here.


class Partners(models.Model):
    """docstring for Partners"""
    class Meta:
        verbose_name = u'Партнер'
        verbose_name_plural = u'Партнеры'
    title = models.CharField(max_length=45)
    slug = models.SlugField(max_length=45)
    description = models.TextField()
    image = models.ImageField(upload_to='partners/images', null=True)
    show = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
