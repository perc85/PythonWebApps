# Generated by Django 5.1.3 on 2024-11-28 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_superhero_is_default_alter_superhero_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superhero',
            name='image',
        ),
        migrations.CreateModel(
            name='SuperheroImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='superheroes/')),
                ('superhero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='articles.superhero')),
            ],
        ),
    ]
