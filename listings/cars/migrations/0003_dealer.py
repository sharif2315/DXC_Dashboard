# Generated by Django 3.0.4 on 2020-03-19 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20200319_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.Car')),
            ],
        ),
    ]
