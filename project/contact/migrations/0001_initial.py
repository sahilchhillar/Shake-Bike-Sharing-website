# Generated by Django 3.1.3 on 2021-02-09 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bikeCode', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]
