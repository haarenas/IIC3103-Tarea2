# Generated by Django 3.0.5 on 2020-04-30 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamburguesa',
            name='imagen',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='hamburguesa',
            name='ingredientes',
            field=models.ManyToManyField(blank=True, to='burger_service.Ingrediente'),
        ),
    ]
