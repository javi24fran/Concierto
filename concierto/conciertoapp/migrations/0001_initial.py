# Generated by Django 3.2 on 2024-10-28 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Categoria', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=50)),
                ('Numero_asiento', models.IntegerField()),
                ('Precio', models.IntegerField()),
                ('Sector', models.CharField(max_length=50)),
            ],
        ),
    ]
