# Generated by Django 2.2.6 on 2019-10-31 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_dislikes_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dislikes',
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
        migrations.AddField(
            model_name='postprod',
            name='dislike',
            field=models.PositiveIntegerField(default=0, verbose_name='Дизлайк'),
        ),
        migrations.AddField(
            model_name='postprod',
            name='like',
            field=models.PositiveIntegerField(default=0, verbose_name='Лайк'),
        ),
    ]
