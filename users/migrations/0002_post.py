# Generated by Django 3.2.5 on 2021-07-25 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('rasm', models.ImageField(upload_to='')),
                ('body', models.TextField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
