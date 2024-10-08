# Generated by Django 4.2.14 on 2024-08-24 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets_management', '0005_assessmentcategory_assessmentquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetlisting',
            name='availability',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assetlisting',
            name='confidentiality',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assetlisting',
            name='integrity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assetlisting',
            name='risk_index',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
