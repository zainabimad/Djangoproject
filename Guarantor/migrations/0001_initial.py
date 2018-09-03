# Generated by Django 2.0.6 on 2018-08-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddGu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True)),
                ('birth_date', models.DateField(null=True)),
                ('number', models.CharField(blank=True, max_length=12)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('img', models.FileField(upload_to='docs/')),
                ('work', models.CharField(max_length=100)),
                ('work_locations', models.CharField(blank=True, max_length=100)),
                ('work_price', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
