# Generated by Django 4.2.14 on 2024-08-16 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets_management', '0002_assetlisting'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetlisting',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]