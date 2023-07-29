# Generated by Django 4.2.3 on 2023-07-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=70)),
                ('lastName', models.CharField(default='', max_length=200)),
                ('email', models.CharField(blank=True, default='', max_length=50)),
                ('mobile', models.CharField(blank=True, default='', max_length=10)),
            ],
        ),
    ]
