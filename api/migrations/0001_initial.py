# Generated by Django 2.0 on 2017-12-31 01:50

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CloudProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_certificate_data', models.CharField(max_length=2000)),
                ('client_key_data', models.CharField(max_length=3000)),
                ('completed', models.DateTimeField(blank=True, null=True)),
                ('features', django.contrib.postgres.fields.jsonb.JSONField()),
                ('settings', django.contrib.postgres.fields.jsonb.JSONField()),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField()),
                ('num_master_nodes', models.IntegerField()),
                ('num_compute_nodes', models.IntegerField()),
                ('requested', models.DateTimeField(auto_now=True)),
                ('version', models.CharField(max_length=128)),
                ('cloud_provider', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.CloudProvider')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('cloud_provider', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.CloudProvider')),
            ],
        ),
        migrations.AddField(
            model_name='cluster',
            name='region',
            field=models.ForeignKey(db_column='region', on_delete=django.db.models.deletion.DO_NOTHING, to='api.Region', to_field='name'),
        ),
    ]
