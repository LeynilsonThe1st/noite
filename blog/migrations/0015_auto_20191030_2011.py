# Generated by Django 2.2.6 on 2019-10-30 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20191030_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacao',
            name='imagem',
            field=models.ImageField(upload_to='blog/static/blog/images/'),
        ),
    ]
