# Generated by Django 5.1.3 on 2024-11-28 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_investigator'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigator',
            name='biography',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='investigator',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
