# Generated by Django 4.2.5 on 2023-10-08 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bebida', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.TextField()),
                ('fotos', models.ImageField(upload_to='coolers')),
                ('itens_cooler', models.ManyToManyField(related_name='itens', to='bebida.bebida')),
            ],
        ),
    ]
