# Generated by Django 4.1.1 on 2022-10-09 22:20

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_cartype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('BranchID', models.AutoField(primary_key=True, serialize=False)),
                ('PhoneNum', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
    ]
