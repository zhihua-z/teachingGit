# Generated by Django 3.2.18 on 2023-08-25 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]
