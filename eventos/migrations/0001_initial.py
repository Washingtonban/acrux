# Generated by Django 3.1.1 on 2020-10-26 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('data_hora', models.DateTimeField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Evento', to='produtos.produto')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
