# Generated by Django 4.2.5 on 2024-03-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_reg', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time_in', models.TimeField()),
                ('time_out', models.TimeField()),
                ('speedometer_reading', models.FloatField()),
                ('km', models.FloatField()),
                ('detail_of_journey', models.TextField()),
                ('order_no', models.CharField(max_length=50)),
                ('driver_signature', models.CharField(max_length=100)),
                ('litres_petrol', models.FloatField()),
                ('militres_oil', models.FloatField()),
                ('remarks', models.TextField()),
            ],
        ),
    ]
