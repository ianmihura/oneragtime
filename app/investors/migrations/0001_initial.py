# Generated by Django 4.0.8 on 2022-10-11 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investors',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('address', models.TextField()),
                ('credit', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
