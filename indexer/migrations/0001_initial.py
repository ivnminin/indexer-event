# Generated by Django 4.1.4 on 2022-12-19 19:57

from django.db import migrations, models
import django.db.models.deletion


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
                ('address', models.CharField(max_length=42, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventBought',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_address', models.CharField(max_length=42)),
                ('amount', models.CharField(max_length=255)),
                ('tx', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EventTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_from', models.CharField(max_length=42)),
                ('to', models.CharField(max_length=42)),
                ('amount', models.CharField(max_length=255)),
                ('tx', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.IntegerField(choices=[(1, 'Bought'), (2, 'Transfer')])),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='indexer.contract')),
            ],
        ),
    ]
