# Generated by Django 4.2.3 on 2023-07-29 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='a', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
