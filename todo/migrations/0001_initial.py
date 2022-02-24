# Generated by Django 4.0.2 on 2022-02-23 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('iscomplete', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]