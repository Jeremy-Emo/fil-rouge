# Generated by Django 2.1.7 on 2019-06-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_commentaries_movie_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentaries',
            options={'verbose_name': 'Commentaire', 'verbose_name_plural': 'Commentaires'},
        ),
        migrations.AlterModelOptions(
            name='favorites',
            options={'verbose_name': 'Favori', 'verbose_name_plural': 'Favoris'},
        ),
        migrations.AddField(
            model_name='commentaries',
            name='text',
            field=models.TextField(blank=True, default=''),
        ),
    ]
