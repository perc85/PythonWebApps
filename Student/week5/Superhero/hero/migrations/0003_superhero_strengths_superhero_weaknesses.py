# Generated by Django 5.1.1 on 2024-10-07 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_superhero_slug_alter_superhero_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='strengths',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='superhero',
            name='weaknesses',
            field=models.TextField(blank=True, null=True),
        ),
    ]
