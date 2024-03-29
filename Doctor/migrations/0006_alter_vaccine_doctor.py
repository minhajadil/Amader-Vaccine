# Generated by Django 5.0.1 on 2024-01-25 08:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_accountmodel_email_token_accountmodel_is_activated'),
        ('Doctor', '0005_vaccine_images_vaccine_precautions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.accountmodel'),
        ),
    ]
