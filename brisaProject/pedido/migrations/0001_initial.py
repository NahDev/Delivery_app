# Generated by Django 4.2.5 on 2023-10-08 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cooler', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('status_entrega', models.CharField(choices=[('em_andamento', 'Em Andamento'), ('entregue', 'Entregue'), ('atrasado', 'Atrasado')], default='em_andamento', max_length=20)),
                ('status_pagamento', models.CharField(choices=[('pago', 'Pago'), ('em_aberto', 'Em Aberto'), ('atrasado', 'Atrasado')], default='em_aberto', max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cooler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooler.cooler')),
            ],
        ),
    ]
