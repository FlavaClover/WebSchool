# Generated by Django 3.2.4 on 2021-07-09 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]