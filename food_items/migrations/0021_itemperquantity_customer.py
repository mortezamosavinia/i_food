# Generated by Django 3.1.3 on 2020-11-25 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201110_2105'),
        ('food_items', '0020_auto_20201125_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemperquantity',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.customer'),
        ),
    ]