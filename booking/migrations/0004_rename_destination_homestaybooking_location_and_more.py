# Generated by Django 5.1.2 on 2025-03-25 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_flightbooking_homestaybooking_hotelbooking_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homestaybooking',
            old_name='destination',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='hotelbooking',
            old_name='destination',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='flightbooking',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='homestaybooking',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='hotelbooking',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='packagebooking',
            name='created_at',
        ),
        migrations.AddField(
            model_name='flightbooking',
            name='airline_name',
            field=models.CharField(default='Flight', max_length=100),
        ),
        migrations.AddField(
            model_name='homestaybooking',
            name='name',
            field=models.CharField(default='Home', max_length=100),
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='name',
            field=models.CharField(default='Hotel', max_length=100),
        ),
        migrations.AddField(
            model_name='packagebooking',
            name='name',
            field=models.CharField(default='Holiday', max_length=100),
        ),
        migrations.AlterField(
            model_name='homestaybooking',
            name='guests',
            field=models.IntegerField(),
        ),
    ]
