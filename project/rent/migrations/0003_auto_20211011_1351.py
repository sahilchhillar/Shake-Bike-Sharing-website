# Generated by Django 3.2.7 on 2021-10-11 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_alter_renttable_starttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renttable',
            name='bikeId',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='renttable',
            name='userId',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
