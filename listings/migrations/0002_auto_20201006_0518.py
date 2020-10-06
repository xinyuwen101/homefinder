# Generated by Django 3.1.2 on 2020-10-06 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='realtor',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='garage',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='lot_size',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_6',
        ),
        migrations.AddField(
            model_name='listing',
            name='unit',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(blank=True),
        ),
    ]