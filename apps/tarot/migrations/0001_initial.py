# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-21 22:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('log_reg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FourCardReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tarot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('suit', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('meaning_up', models.CharField(max_length=300)),
                ('meaning_rev', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ThreeCardReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('future', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='future_cards', to='tarot.Tarot')),
                ('past', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='past_cards', to='tarot.Tarot')),
                ('present', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='present_cards', to='tarot.Tarot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='three_card_readings', to='log_reg.User')),
            ],
        ),
        migrations.AddField(
            model_name='fourcardreading',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_cards', to='tarot.Tarot'),
        ),
        migrations.AddField(
            model_name='fourcardreading',
            name='known',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='known_cards', to='tarot.Tarot'),
        ),
        migrations.AddField(
            model_name='fourcardreading',
            name='unknown',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unknown_cards', to='tarot.Tarot'),
        ),
        migrations.AddField(
            model_name='fourcardreading',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='four_card_readings', to='log_reg.User'),
        ),
        migrations.AddField(
            model_name='fourcardreading',
            name='you',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='you_cards', to='tarot.Tarot'),
        ),
    ]
