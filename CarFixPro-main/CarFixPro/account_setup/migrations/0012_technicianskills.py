# Generated by Django 4.2.5 on 2023-11-16 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_setup', '0011_alter_technicianinfo_hourly_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechnicianSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.EmailField(max_length=254)),
                ('service_type', models.CharField(max_length=30)),
            ],
        ),
    ]