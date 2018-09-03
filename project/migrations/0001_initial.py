# Generated by Django 2.0.6 on 2018-08-08 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddAc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('detils', models.CharField(blank=True, max_length=100)),
                ('locations', models.CharField(blank=True, max_length=100)),
                ('worked', models.CharField(blank=True, max_length=12)),
                ('up_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Authentic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('superuser', 'superuser'), ('user', 'user'), ('admin', 'admin')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]