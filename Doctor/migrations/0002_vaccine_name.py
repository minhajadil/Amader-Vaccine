# Generated by Django 5.0.1 on 2024-01-20 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccine',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
