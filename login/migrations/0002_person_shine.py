# Generated by Django 2.2.1 on 2019-06-15 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='shine',
            field=models.CharField(max_length=100, null=True, verbose_name='Шины'),
        ),
    ]