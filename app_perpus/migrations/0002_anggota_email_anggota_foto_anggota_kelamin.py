# Generated by Django 5.0 on 2023-12-11 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_perpus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anggota',
            name='email',
            field=models.CharField(default='anggota@gmail.com', max_length=20),
        ),
        migrations.AddField(
            model_name='anggota',
            name='foto',
            field=models.ImageField(default=False, upload_to='img'),
        ),
        migrations.AddField(
            model_name='anggota',
            name='kelamin',
            field=models.CharField(choices=[('Laki-Laki', 'Laki-Laki'), ('Perempuan', 'Perempuan')], default=True, max_length=10),
            preserve_default=False,
        ),
    ]
