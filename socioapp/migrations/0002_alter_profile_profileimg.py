# Generated by Django 3.2.6 on 2021-09-18 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socioapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='profile_images/blank-profile-picture.png', upload_to='profile_images'),
        ),
    ]
