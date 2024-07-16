# Generated by Django 5.0.6 on 2024-07-12 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_alter_albummodel_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummodel',
            name='rating',
            field=models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], max_length=1),
        ),
    ]