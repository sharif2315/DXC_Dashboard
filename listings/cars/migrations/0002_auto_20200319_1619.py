# Generated by Django 3.0.4 on 2020-03-19 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuelType',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='gearBox',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='notRepairedDamage',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='vehicleType',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
