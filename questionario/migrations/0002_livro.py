# Generated by Django 5.1 on 2024-08-28 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=200)),
            ],
        ),
    ]
