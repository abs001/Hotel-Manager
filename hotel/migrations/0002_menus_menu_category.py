# Generated by Django 2.2 on 2020-04-26 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menus',
            name='menu_category',
            field=models.ForeignKey(default='Other', on_delete=django.db.models.deletion.CASCADE, to='hotel.MenuCategory'),
        ),
    ]
