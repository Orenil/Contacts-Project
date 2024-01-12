# Generated by Django 4.2.7 on 2024-01-12 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0029_alter_contact_options_remove_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign_emails',
            name='campaign_name',
            field=models.CharField(db_index=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='campaign_emails',
            name='company',
            field=models.CharField(db_index=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='campaign_emails',
            name='first_name',
            field=models.CharField(db_index=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='campaign_emails',
            name='last_name',
            field=models.CharField(db_index=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='campaign_emails',
            name='location',
            field=models.CharField(db_index=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='campaign_emails',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='campaign_emails',
            name='type',
            field=models.CharField(db_index=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='company',
            field=models.CharField(db_index=True, default='No Company', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(db_index=True, default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(db_index=True, default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='level',
            field=models.CharField(db_index=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='location',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(db_index=True, default='No Title', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.CharField(db_index=True, default='None', max_length=100),
        ),
    ]
