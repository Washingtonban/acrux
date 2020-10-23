# Generated by Django 3.1.1 on 2020-10-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=255)),
                ('preco', models.FloatField(max_length=255)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='../media/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
