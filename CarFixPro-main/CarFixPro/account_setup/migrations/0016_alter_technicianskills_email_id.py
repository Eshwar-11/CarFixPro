# Generated by Django 4.2.5 on 2023-11-21 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_setup', '0015_alter_appointmentstatus_completed_by_technician'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicianskills',
            name='email_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_setup.technicianinfo'),
        ),
    ]
