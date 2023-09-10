# Generated by Django 3.2.20 on 2023-09-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True)),
                ('industry', models.CharField(blank=True, max_length=100)),
                ('headquarters', models.CharField(blank=True, max_length=100)),
                ('website', models.URLField(blank=True)),
            ],
        ),
    ]