# Generated by Django 3.1.3 on 2020-11-28 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0036_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='item',
            field=models.CharField(default='', max_length=150),
        ),
    ]
