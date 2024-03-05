# Generated by Django 5.0.2 on 2024-03-01 05:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airveys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Samalyot',
                'verbose_name_plural': 'Samalyotlar',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Shaharlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='shaharlar/')),
                ('text', models.TextField(max_length=900)),
                ('airveys', models.ManyToManyField(blank=True, null=True, to='student.airveys')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.category')),
            ],
            options={
                'verbose_name': 'shahar',
                'verbose_name_plural': 'shaharlar',
            },
        ),
    ]