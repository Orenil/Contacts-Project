# Generated by Django 4.2.7 on 2024-01-29 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0036_remove_email_campaign_name_email_campaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='campaign',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contacts.campaign'),
        ),
    ]