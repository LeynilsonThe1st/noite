# Generated by Django 2.2.6 on 2019-10-30 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20191030_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacao',
            name='imagem',
            field=models.ImageField(upload_to='', verbose_name='blog/static/images/'),
        ),
    ]