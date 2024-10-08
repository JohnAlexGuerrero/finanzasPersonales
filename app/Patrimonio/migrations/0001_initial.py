# Generated by Django 5.1.1 on 2024-09-17 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Active',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_fijo', models.BooleanField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
                ('type', models.CharField(choices=[('Tangibles', 'Tangible'), ('No Tangibles', 'In Tangible')], max_length=150)),
                ('category', models.CharField(choices=[('Inventarios', 'Inventarios'), ('Propiedades', 'Propiedades'), ('Equipo', 'Equipo'), ('Vehiculos', 'Vehiculos'), ('Ahorros', 'Ahorro'), ('Titulos de Valor', 'Titulos Valor')], max_length=150)),
            ],
            options={
                'verbose_name': 'Active',
                'verbose_name_plural': 'Actives',
            },
        ),
        migrations.CreateModel(
            name='Passive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_fijo', models.BooleanField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
                ('type', models.CharField(choices=[('Tangibles', 'Tangible'), ('No Tangibles', 'In Tangible')], max_length=150)),
                ('category', models.CharField(choices=[('Creditos', 'Credito'), ('Proveedores', 'Proveedores'), ('Equipo', 'Equipo'), ('Vehiculos', 'Vehiculos'), ('Propiedades', 'Propiedades')], max_length=150)),
            ],
            options={
                'verbose_name': 'Passive',
                'verbose_name_plural': 'Passive',
            },
        ),
    ]
