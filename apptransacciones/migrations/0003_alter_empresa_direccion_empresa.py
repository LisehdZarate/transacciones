# Generated by Django 4.1 on 2022-09-25 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptransacciones', '0002_cargo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='direccion_Empresa',
            field=models.CharField(max_length=255),
        ),
    ]