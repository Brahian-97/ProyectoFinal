# Generated by Django 4.1 on 2022-10-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depto', '0003_integrantes_depto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrantes',
            name='depto',
            field=models.CharField(max_length=30),
        ),
    ]
