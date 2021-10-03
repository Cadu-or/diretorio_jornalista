# Generated by Django 3.2.7 on 2021-10-03 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nome', models.CharField(max_length=65, primary_key=True, serialize=False)),
                ('data_nascimento', models.DateField()),
                ('raça_etnia', models.CharField(max_length=45)),
                ('genero', models.CharField(blank=True, max_length=30, null=True)),
                ('estado_civil', models.CharField(blank=True, max_length=15, null=True)),
                ('cidade', models.CharField(blank=True, max_length=30, null=True)),
                ('estado', models.CharField(blank=True, max_length=15, null=True)),
                ('funcao', models.IntegerField(blank=True, choices=[(4, 'Usuario'), (3, 'Jornalista'), (1, 'Admin'), (2, 'Revisor')], null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
    ]
