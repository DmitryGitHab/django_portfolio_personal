from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True,)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title

class Stack(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True,)
    image = models.ImageField(upload_to='portfolio/stack_images')
    date = models.DateField()

    def __str__(self):
        return self.title

class Сertificate(models.Model):
    class Meta:
        db_table = 'certificates'

    # img = models.CharField(max_length=120, verbose_name='Файл картинки')
    img = models.ImageField(upload_to='portfolio/cert_images')
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    sub_title = models.TextField(verbose_name='Описание', null=True,)
    alt = models.TextField(verbose_name='Подсказка', null=True,)
    index = models.IntegerField(verbose_name='Индекс')

    def __unicode__(self):
        return self.title