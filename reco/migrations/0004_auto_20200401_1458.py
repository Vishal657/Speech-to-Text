# Generated by Django 3.0.3 on 2020-04-01 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reco', '0003_auto_20200401_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
