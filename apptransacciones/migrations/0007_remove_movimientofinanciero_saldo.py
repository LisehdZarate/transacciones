# Generated by Django 4.1 on 2022-09-26 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptransacciones', '0006_remove_usuario_usuemp_empresausuario_uniqueuser_emp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimientofinanciero',
            name='saldo',
        ),
    ]
