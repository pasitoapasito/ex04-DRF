# Generated by Django 4.0.7 on 2022-09-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
