# Generated by Django 3.0.2 on 2020-02-02 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adrress1', models.CharField(max_length=150)),
                ('adrress2', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=70)),
                ('latitude', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
