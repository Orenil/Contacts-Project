# Generated by Django 4.2.7 on 2024-01-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0030_alter_campaign_emails_campaign_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='linkedin',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='campaign_emails',
            name='campaign_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='campaign_emails',
            name='company',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='campaign_emails',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='campaign_emails',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='campaign_emails',
            name='location',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='campaign_emails',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='campaign_emails',
            name='type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='company',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='level',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.CharField(default='', max_length=100),
        ),
    ]
