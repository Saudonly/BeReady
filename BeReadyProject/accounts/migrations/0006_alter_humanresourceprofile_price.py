# Generated by Django 4.1.3 on 2022-11-14 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_humanresourceprofile_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humanresourceprofile',
            name='price',
            field=models.CharField(max_length=32),
        ),
    ]
