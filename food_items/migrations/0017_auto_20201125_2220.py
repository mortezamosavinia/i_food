# Generated by Django 3.1.3 on 2020-11-25 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0016_auto_20201125_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='itemperquantity',
        ),
        migrations.AddField(
            model_name='cart',
            name='itemperquantity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itemperquantity', to='food_items.itemperquantity'),
        ),
    ]