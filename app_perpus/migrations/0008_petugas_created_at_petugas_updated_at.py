# Generated by Django 5.0 on 2023-12-14 09:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_perpus', '0007_buku_created_at_buku_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='petugas',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='petugas',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
