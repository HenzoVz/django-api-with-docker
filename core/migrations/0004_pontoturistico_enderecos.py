# Generated by Django 3.0.2 on 2020-02-02 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0002_auto_20200202_2113'),
        ('core', '0003_pontoturistico_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='enderecos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enderecos.Endereco'),
            preserve_default=False,
        ),
    ]