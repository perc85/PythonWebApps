# Generated by Django 5.1.2 on 2024-10-16 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='image',
            field=models.CharField(default='default.jpg', max_length=100),
        ),
    ]
