# Generated by Django 2.1.5 on 2019-03-12 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0009_auto_20190227_1000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('class_id',)},
        ),
    ]
