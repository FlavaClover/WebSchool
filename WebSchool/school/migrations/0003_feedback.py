# Generated by Django 3.2.4 on 2021-07-04 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_news_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField(max_length=5555)),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
