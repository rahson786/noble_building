# Generated by Django 4.1.1 on 2022-10-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noble_building_llc', '0002_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='people',
            name='designation',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
