# Generated by Django 2.2 on 2019-04-28 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190428_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='767039450401304849', max_length=255, primary_key=True, serialize=False),
        ),
    ]
