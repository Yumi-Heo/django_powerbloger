# Generated by Django 4.2.5 on 2023-09-18 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_blogpost_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
