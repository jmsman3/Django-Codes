# Generated by Django 5.0.6 on 2024-07-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0006_carmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
