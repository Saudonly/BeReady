# Generated by Django 4.1.3 on 2022-11-14 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_humanresourceprofile_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='humanresourceprofile',
            name='card_number',
            field=models.IntegerField(default=4201322020575830),
            preserve_default=False,
        ),
    ]
