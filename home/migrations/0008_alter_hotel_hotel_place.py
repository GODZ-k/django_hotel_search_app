# Generated by Django 4.2.4 on 2023-10-20 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_hotel_hotel_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel_place',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
