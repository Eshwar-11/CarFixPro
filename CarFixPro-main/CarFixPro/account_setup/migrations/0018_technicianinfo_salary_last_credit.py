# Generated by Django 4.2.5 on 2023-11-21 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_setup', '0017_alter_appointmentstatus_completed_by_technician'),
    ]

    operations = [
        migrations.AddField(
            model_name='technicianinfo',
            name='salary_last_credit',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
