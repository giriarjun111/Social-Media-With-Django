# Generated by Django 4.0.6 on 2022-07-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0014_alter_userprofile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='uploads/profile_pictures/default.jpg', upload_to='uploads/profile_pictures'),
        ),
    ]