# Generated by Django 4.2.7 on 2023-12-13 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='client_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='')),
                ('position', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='client_logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=350)),
                ('message', models.TextField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
