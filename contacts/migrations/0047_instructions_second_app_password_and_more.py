# Generated by Django 4.2.7 on 2024-02-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0046_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructions',
            name='second_app_password',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='instructions',
            name='second_email',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='instructions',
            name='third_app_password',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='instructions',
            name='third_email',
            field=models.TextField(default=''),
        ),
    ]
