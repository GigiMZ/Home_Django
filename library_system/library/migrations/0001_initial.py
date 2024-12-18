# Generated by Django 5.1.3 on 2024-11-08 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('joined_date', models.DateField()),
                ('book_id', models.ManyToManyField(related_name='book_id', to='library.book')),
                ('lib_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='members_id', to='library.library')),
            ],
        ),
        migrations.CreateModel(
            name='LibraryCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=100)),
                ('issued_date', models.DateField()),
                ('member_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='card', to='library.member')),
            ],
        ),
    ]
