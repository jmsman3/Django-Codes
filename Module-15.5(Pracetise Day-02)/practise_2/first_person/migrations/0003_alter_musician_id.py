# Generated by Django 5.0.6 on 2024-07-03 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_person', '0002_rename_album_name_albummodel_musician_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
