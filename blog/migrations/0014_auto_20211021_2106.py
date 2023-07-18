# Generated by Django 3.1.5 on 2021-10-21 19:06

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20211021_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategorimodel',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='isim', unique=True),
        ),
        migrations.AlterField(
            model_name='yazilarmodel',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='baslik', unique=True),
        ),
    ]