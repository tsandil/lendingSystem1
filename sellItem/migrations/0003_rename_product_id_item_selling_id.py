# Generated by Django 3.2.7 on 2021-10-31 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellItem', '0002_auto_20211031_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='product_id',
            new_name='selling_id',
        ),
    ]
