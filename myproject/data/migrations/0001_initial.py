# Generated by Django 3.0.8 on 2020-10-12 20:25

import datetime
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
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('title', models.CharField(max_length=64)),
                ('summary', models.CharField(max_length=10000)),
                ('ipAddress', models.CharField(max_length=15)),
                ('date', models.DateField(default=datetime.date.today)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='data.Company')),
                ('reviewer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]