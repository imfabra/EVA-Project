# Generated by Django 4.2.2 on 2023-06-13 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('etiqueta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_crud.etiqueta')),
            ],
        ),
        migrations.CreateModel(
            name='Submovimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join1', models.DecimalField(decimal_places=2, max_digits=16)),
                ('join2', models.DecimalField(decimal_places=2, max_digits=16)),
                ('join3', models.DecimalField(decimal_places=2, max_digits=16)),
                ('join4', models.DecimalField(decimal_places=2, max_digits=16)),
                ('join5', models.DecimalField(decimal_places=2, max_digits=16)),
                ('velocidad', models.DecimalField(decimal_places=2, max_digits=16)),
                ('tiempo', models.DecimalField(decimal_places=2, max_digits=16)),
                ('orden', models.IntegerField()),
                ('movimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_crud.movimiento')),
            ],
        ),
    ]
