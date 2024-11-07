# Generated by Django 5.1.2 on 2024-10-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('identity', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('strength', models.CharField(max_length=100)),
                ('weakness', models.CharField(max_length=100)),
                ('image', models.CharField(default='images/default.jpg', max_length=100)),
            ],
        ),
    ]