# Generated by Django 2.2.9 on 2020-02-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]