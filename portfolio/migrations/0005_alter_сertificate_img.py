# Generated by Django 4.0.5 on 2022-10-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_сertificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='сertificate',
            name='img',
            field=models.ImageField(upload_to='portfolio/cert_images'),
        ),
    ]
