from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField()
    date = models.DateField()


    def __str__(self):
        return self.title

    # image = models.ImageField(upload_to='portfolio/images')
    # url = models.URLField(blank=True)
