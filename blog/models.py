from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    # image = models.ImageField(upload_to='portfolio/images')
    # url = models.URLField(blank=True)
