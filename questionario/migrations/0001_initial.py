# Generated by Django 5.0.7 on 2024-08-07 21:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcao', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Alternativa',
            },
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=200)),
                ('alternativas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionario.alternativa')),
            ],
            options={
                'verbose_name': 'Questõe',
            },
        ),
    ]
