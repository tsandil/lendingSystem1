# Generated by Django 3.2.7 on 2021-10-31 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellItem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.AddField(
            model_name='item',
            name='product_id',
            field=models.BigAutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
