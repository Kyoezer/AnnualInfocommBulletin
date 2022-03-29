# Generated by Django 3.0 on 2022-03-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20220323_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dzongkhag',
            fields=[
                ('dzoID', models.IntegerField(primary_key=True, serialize=False)),
                ('dzongkhagNames', models.CharField(max_length=100)),
                ('gewogs', models.CharField(max_length=100)),
                ('isRegion', models.CharField(max_length=1)),
                ('createdDateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegionDetails',
            fields=[
                ('regionID', models.IntegerField(primary_key=True, serialize=False)),
                ('regionName', models.CharField(max_length=100)),
                ('createdDateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
