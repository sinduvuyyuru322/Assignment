# Generated by Django 5.1.2 on 2024-11-03 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.EmailField(default='emailid@example.com', max_length=254)),
                ('passward', models.TextField(max_length=10)),
                ('conform', models.TextField(max_length=10)),
            ],
        ),
    ]
