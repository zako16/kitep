from django.db import models


class Slides(models.Model):
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
    slide = models.ImageField(upload_to='slider/slides')
    title = models.CharField(max_length=45)
    show = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
