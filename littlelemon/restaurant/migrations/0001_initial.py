# Generated by Django 4.1.4 on 2023-11-07 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=225)),
                ('No_of_guest', models.IntegerField()),
                ('BookingDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=225)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Inventory', models.IntegerField()),
            ],
        ),
    ]