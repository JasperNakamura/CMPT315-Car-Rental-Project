# Generated by Django 4.1.1 on 2022-10-10 00:00

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_employee_city_employee_dob_employee_postalcode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('DriversLicense', models.PositiveIntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('PhoneNum', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('DOB', models.DateField()),
                ('GoldMember', models.BooleanField(default=False)),
                ('Province', models.CharField(max_length=25)),
                ('City', models.CharField(max_length=25)),
                ('PostalCode', models.CharField(max_length=6)),
                ('StreetNumber', models.PositiveSmallIntegerField()),
                ('StreetName', models.CharField(max_length=15)),
                ('UnitNumber', models.PositiveSmallIntegerField(blank=True)),
            ],
        ),
    ]
