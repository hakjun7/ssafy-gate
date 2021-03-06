# Generated by Django 2.2.6 on 2020-07-30 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'articles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pros',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('userid', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'pros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProSurveys',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=200)),
                ('checked', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'pro_surveys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'regions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('class_field', models.BigIntegerField(db_column='class')),
                ('profile_img', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'students',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Surveys',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('body_temperature', models.FloatField()),
                ('danger', models.IntegerField()),
                ('body_check', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'surveys',
                'managed': False,
            },
        ),
    ]
