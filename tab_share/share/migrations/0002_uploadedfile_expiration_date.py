# Generated by Django 5.0.7 on 2024-07-16 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='expiration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
