# Generated by Django 5.1 on 2024-09-03 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0003_veiculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
