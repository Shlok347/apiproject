# Generated by Django 2.1.7 on 2019-05-29 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('master_password', models.CharField(max_length=64)),
            ],
        ),
    ]
