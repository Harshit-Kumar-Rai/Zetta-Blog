# Generated by Django 4.1.7 on 2023-08-08 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.TextField(null=True),
        ),
    ]
