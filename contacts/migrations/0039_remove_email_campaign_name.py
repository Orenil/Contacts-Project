# Generated by Django 4.2.7 on 2024-01-29 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0038_remove_email_campaign_email_campaign_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='campaign_name',
        ),
    ]
