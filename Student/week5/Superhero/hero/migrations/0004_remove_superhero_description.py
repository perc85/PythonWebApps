# Generated by Django 5.1.1 on 2024-10-07 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_superhero_strengths_superhero_weaknesses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superhero',
            name='description',
        ),
    ]
