# Generated by Django 5.0.1 on 2024-01-20 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Doctor', '0003_alter_vaccine_initial_dose'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccineTaken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.vaccine')),
            ],
        ),
    ]
