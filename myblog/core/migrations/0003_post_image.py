# Generated by Django 2.1.5 on 2019-01-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/images', verbose_name='Imagem'),
        ),
    ]
