# Generated by Django 3.0.5 on 2021-03-03 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('link', models.TextField()),
                ('source', models.TextField()),
                ('img', models.TextField()),
            ],
        ),
    ]