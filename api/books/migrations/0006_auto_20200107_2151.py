# Generated by Django 3.0.2 on 2020-01-07 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20200107_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='amazon_link',
            field=models.CharField(max_length=512),
        ),
    ]
