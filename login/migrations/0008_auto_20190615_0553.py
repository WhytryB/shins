# Generated by Django 2.2.1 on 2019-06-15 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20190615_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='iznos1',
            field=models.IntegerField(null=True, verbose_name='Износ 1'),
        ),
        migrations.AlterField(
            model_name='person',
            name='iznos2',
            field=models.IntegerField(max_length=100, null=True, verbose_name='Износ 2'),
        ),
        migrations.AlterField(
            model_name='person',
            name='iznos3',
            field=models.IntegerField(max_length=100, null=True, verbose_name='Износ 3'),
        ),
        migrations.AlterField(
            model_name='person',
            name='iznos4',
            field=models.IntegerField(max_length=100, null=True, verbose_name='Износ 4'),
        ),
    ]