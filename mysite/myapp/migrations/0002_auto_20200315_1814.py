# Generated by Django 3.0.3 on 2020-03-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary_model',
            name='summary',
            field=models.CharField(max_length=180),
        ),
    ]
