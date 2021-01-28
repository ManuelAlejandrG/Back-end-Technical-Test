# Generated by Django 3.1.5 on 2021-01-28 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemones',
            name='min_level',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pokemones',
            name='needs_overworld_rain',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='pokemones',
            name='turn_upside_down',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='pokemones',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
