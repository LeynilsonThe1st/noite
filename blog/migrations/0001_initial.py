# Generated by Django 2.2.6 on 2019-10-19 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('criado_em', models.DateTimeField(verbose_name='Data de criação')),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='Última alteração')),
                ('autor', models.CharField(max_length=200)),
                ('body', models.TextField()),
            ],
        ),
    ]
