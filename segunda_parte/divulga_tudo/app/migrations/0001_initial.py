# Generated by Django 3.2.4 on 2021-06-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_anuncio', models.CharField(max_length=150)),
                ('nome_cliente', models.CharField(max_length=150)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('investimento_dia', models.DecimalField(decimal_places=2, max_digits=100)),
            ],
        ),
    ]
