# Generated by Django 2.1.5 on 2019-01-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakenews_api', '0003_auto_20190119_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='content',
            field=models.TextField(),
        ),
    ]
