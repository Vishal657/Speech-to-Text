# Generated by Django 3.0.3 on 2020-04-01 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0002_auto_20200401_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
