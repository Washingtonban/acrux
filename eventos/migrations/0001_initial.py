# Generated by Django 3.1.1 on 2020-10-23 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0001_initial'),
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pessoa.pessoa')),
            ],
            options={
                'abstract': False,
            },
            bases=('pessoa.pessoa',),
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('produto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='produtos.produto')),
            ],
            options={
                'abstract': False,
            },
            bases=('produtos.produto',),
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('data_hora', models.DateTimeField()),
                ('Pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Evento', to='eventos.pessoa')),
                ('Produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Evento', to='eventos.produto')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
