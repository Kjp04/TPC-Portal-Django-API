# Generated by Django 3.2.8 on 2022-03-12 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpc_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(default='dypatil@123', max_length=50),
        ),
    ]
