from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=32, verbose_name='Название категории')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'категории'
        verbose_name = 'категорию'

    def __str__(self):
        return self.category_name

class Theme(models.Model):
    theme_name = models.CharField(max_length=32, verbose_name='Название категории')
    add_time = models.DateTimeField(auto_now_add=True)
    theme_description = models.TextField(verbose_name='Описание')
    theme_photo = models.ImageField(upload_to='media', verbose_name= 'Фото')
    theme_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'статьи'
        verbose_name = 'статью'

    def __str__(self):
        return self.theme_name
