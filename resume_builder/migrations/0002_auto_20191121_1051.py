# Generated by Django 2.2.5 on 2019-11-21 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_builder', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': (('-end_date', '-start_date'),)},
        ),
    ]
