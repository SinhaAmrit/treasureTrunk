# Generated by Django 3.2 on 2024-01-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20240108_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreviews',
            name='rating',
            field=models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], default=None),
        ),
    ]
