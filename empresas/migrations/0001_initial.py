# Generated by Django 3.1.1 on 2020-10-26 21:35

from django.db import migrations, models
import django_enumfield.db.fields
import empresas.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('cnpj', models.IntegerField()),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.IntegerField()),
                ('grupo', django_enumfield.db.fields.EnumField(enum=empresas.models.AtributoEmpresa)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
