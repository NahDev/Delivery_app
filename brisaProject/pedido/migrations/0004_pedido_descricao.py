# Generated by Django 4.2.5 on 2023-10-10 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_pedido_coordenadas'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='descricao',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]