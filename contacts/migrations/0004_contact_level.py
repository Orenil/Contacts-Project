# Generated by Django 4.2.7 on 2023-12-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_rename_name_contact_location_contact_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='level',
            field=models.CharField(default='None', max_length=100),
        ),
    ]