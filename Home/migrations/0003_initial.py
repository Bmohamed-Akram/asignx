# Generated by Django 4.2.7 on 2023-12-13 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0002_delete_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=300)),
                ('service', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=2000)),
                ('link', models.URLField()),
            ],
        ),
    ]
