# Generated by Django 4.2.7 on 2024-01-30 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0042_email_font_family_email_font_size_email_is_bold_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='font_family',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='font_size',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
