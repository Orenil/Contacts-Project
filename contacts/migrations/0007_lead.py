# Generated by Django 4.2.7 on 2023-12-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_alter_contact_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=50)),
            ],
        ),
    ]
