# Generated by Django 4.2.7 on 2024-01-29 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0035_email_campaign_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='campaign_name',
        ),
        migrations.AddField(
            model_name='email',
            name='campaign',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='contacts.campaign'),
        ),
    ]