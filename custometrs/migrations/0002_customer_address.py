# Generated by Django 5.0.7 on 2024-08-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custometrs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
