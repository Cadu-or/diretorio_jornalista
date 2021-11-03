# Generated by Django 3.2.7 on 2021-11-02 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0006_auto_20211102_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idioma',
            name='compreende',
            field=models.IntegerField(blank=True, choices=[(4, 'Fluente'), (2, 'Razoavelmente'), (1, 'Pouco'), (3, 'Bem')], null=True),
        ),
        migrations.AlterField(
            model_name='idioma',
            name='escreve',
            field=models.IntegerField(blank=True, choices=[(4, 'Fluente'), (2, 'Razoavelmente'), (1, 'Pouco'), (3, 'Bem')], null=True),
        ),
        migrations.AlterField(
            model_name='idioma',
            name='fala',
            field=models.IntegerField(blank=True, choices=[(4, 'Fluente'), (2, 'Razoavelmente'), (1, 'Pouco'), (3, 'Bem')], null=True),
        ),
        migrations.AlterField(
            model_name='idioma',
            name='ler',
            field=models.IntegerField(blank=True, choices=[(4, 'Fluente'), (2, 'Razoavelmente'), (1, 'Pouco'), (3, 'Bem')], null=True),
        ),
    ]
