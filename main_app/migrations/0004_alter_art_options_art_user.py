# Generated by Django 4.1 on 2022-08-08 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_alter_artist_about'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='art',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='art',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]