# Generated by Django 4.0.1 on 2022-01-30 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointstable',
            name='name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pointstable',
            name='points',
            field=models.CharField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]