# Generated by Django 4.2.4 on 2023-08-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_contactus_data_protection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='data_protection',
            field=models.BooleanField(),
        ),
    ]