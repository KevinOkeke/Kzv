# Generated by Django 3.0.5 on 2020-05-12 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0028_auto_20200511_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe_model',
            name='directions',
            field=models.TextField(blank=True, default='Enter cooking instructions here', null=True),
        ),
    ]
