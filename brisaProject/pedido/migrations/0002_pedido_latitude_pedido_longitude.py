# Generated by Django 4.2.5 on 2023-10-10 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
