# Generated by Django 3.2 on 2022-12-12 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_items'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='carlist',
            new_name='cartlist',
        ),
    ]