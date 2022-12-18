# Generated by Django 4.1.4 on 2022-12-17 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_type', models.IntegerField(choices=[(1, 'Token'), (2, 'Token Sale')])),
                ('name', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=42)),
            ],
        ),
    ]
