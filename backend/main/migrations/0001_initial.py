# Generated by Django 3.1.2 on 2020-10-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPUMetric',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('data', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
