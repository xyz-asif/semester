# Generated by Django 3.0.6 on 2020-05-13 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='branch_icon',
            field=models.ImageField(blank=True, upload_to='images/icons/'),
        ),
    ]
