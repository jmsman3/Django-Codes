# Generated by Django 5.0.6 on 2024-07-14 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0008_alter_carmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='image',
        ),
    ]