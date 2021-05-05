# Generated by Django 3.2 on 2021-05-05 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_authorinfo_outputname'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword_ch', models.CharField(blank=True, max_length=100)),
                ('abstract_ch', models.TextField(blank=True, max_length=1000)),
                ('keyword_en', models.CharField(blank=True, max_length=100)),
                ('abstract_en', models.TextField(blank=True, max_length=1000)),
            ],
        ),
    ]
