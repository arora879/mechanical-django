# Generated by Django 3.0.8 on 2020-08-01 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('services', models.CharField(max_length=260, unique=True)),
            ],
        ),
    ]