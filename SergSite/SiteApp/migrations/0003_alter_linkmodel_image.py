# Generated by Django 4.2.3 on 2023-07-12 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteApp', '0002_linkmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkmodel',
            name='image',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
