# Generated by Django 5.0.7 on 2024-07-22 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_link_gstin_no_link_pan_no_link_permanent_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='permanent_address',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
