# Generated by Django 4.2.4 on 2023-08-13 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_contactus_data_protection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='salutation',
            field=models.CharField(choices=[('herr', 'Herr'), ('frau', 'Frau'), ('noValue', 'Ohne Angabe')], default='herr', max_length=10),
        ),
    ]