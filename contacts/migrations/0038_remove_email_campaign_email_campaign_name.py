# Generated by Django 4.2.7 on 2024-01-29 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0037_alter_email_campaign'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='campaign',
        ),
        migrations.AddField(
            model_name='email',
            name='campaign_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]