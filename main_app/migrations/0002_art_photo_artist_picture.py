# Generated by Django 4.1 on 2022-08-07 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='photo',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='picture',
            field=models.CharField(default=2, max_length=250),
            preserve_default=False,
        ),
    ]
