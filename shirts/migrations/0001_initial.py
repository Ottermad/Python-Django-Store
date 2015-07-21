# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='')),
                ('price', models.FloatField()),
                ('paypal', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='shirt',
            name='sizes',
            field=models.ManyToManyField(to='shirts.Size'),
        ),
    ]
