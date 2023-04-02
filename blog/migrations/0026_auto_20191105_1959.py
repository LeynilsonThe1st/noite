# Generated by Django 2.2.6 on 2019-11-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20191104_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViwerEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='tag',
            name='Publicacao',
        ),
        migrations.AddField(
            model_name='tag',
            name='Publicacao',
            field=models.ManyToManyField(related_name='tags', to='blog.Publicacao'),
        ),
    ]
