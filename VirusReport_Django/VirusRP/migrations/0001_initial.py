# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Virus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('MD5', models.CharField(max_length=128)),
                ('size_KB', models.DecimalField(default=0, max_digits=128, decimal_places=5)),
                ('VirusTotal_link', models.URLField()),
                ('Detection', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
