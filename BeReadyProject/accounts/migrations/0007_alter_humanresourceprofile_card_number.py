# Generated by Django 4.1.3 on 2022-11-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_humanresourceprofile_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humanresourceprofile',
            name='card_number',
            field=models.CharField(max_length=32),
        ),
    ]
