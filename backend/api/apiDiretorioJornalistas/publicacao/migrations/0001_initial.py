# Generated by Django 3.2.7 on 2021-11-02 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('controleDeAcesso', '0004_auto_20211102_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('veiculo', models.IntegerField(choices=[(7, 'Plataforma de Video'), (4, 'TV'), (6, 'Rede Social'), (3, 'Rádio'), (5, 'Site/Blog'), (1, 'Jornal'), (8, 'Podcast'), (2, 'Revista')])),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Coluna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('veiculo', models.IntegerField(choices=[(7, 'Plataforma de Video'), (4, 'TV'), (6, 'Rede Social'), (3, 'Rádio'), (5, 'Site/Blog'), (1, 'Jornal'), (8, 'Podcast'), (2, 'Revista')])),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entrevista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('veiculo', models.IntegerField(choices=[(7, 'Plataforma de Video'), (4, 'TV'), (6, 'Rede Social'), (3, 'Rádio'), (5, 'Site/Blog'), (1, 'Jornal'), (8, 'Podcast'), (2, 'Revista')])),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('veiculo', models.IntegerField(choices=[(7, 'Plataforma de Video'), (4, 'TV'), (6, 'Rede Social'), (3, 'Rádio'), (5, 'Site/Blog'), (1, 'Jornal'), (8, 'Podcast'), (2, 'Revista')])),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reportagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('veiculo', models.IntegerField(choices=[(7, 'Plataforma de Video'), (4, 'TV'), (6, 'Rede Social'), (3, 'Rádio'), (5, 'Site/Blog'), (1, 'Jornal'), (8, 'Podcast'), (2, 'Revista')])),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resenha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('veiculo', models.IntegerField(choices=[(7, 'Plataforma de Video'), (4, 'TV'), (6, 'Rede Social'), (3, 'Rádio'), (5, 'Site/Blog'), (1, 'Jornal'), (8, 'Podcast'), (2, 'Revista')])),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('isbn13', models.CharField(blank=True, max_length=13)),
                ('isbn10', models.CharField(blank=True, max_length=13)),
                ('editora', models.CharField(max_length=100)),
                ('paginas', models.IntegerField(blank=True)),
                ('ano', models.DateField(blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='controleDeAcesso.cidade')),
            ],
        ),
    ]
