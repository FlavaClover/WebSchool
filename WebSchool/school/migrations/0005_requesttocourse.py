# Generated by Django 3.2.4 on 2021-07-13 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestToCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('telegram', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
