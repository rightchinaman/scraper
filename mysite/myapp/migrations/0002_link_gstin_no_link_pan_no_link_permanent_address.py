# Generated by Django 5.0.7 on 2024-07-22 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='gstin_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='link',
            name='pan_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='link',
            name='permanent_address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
