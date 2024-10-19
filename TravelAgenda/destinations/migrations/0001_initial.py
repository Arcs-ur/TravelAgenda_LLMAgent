# Generated by Django 5.1.2 on 2024-10-14 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('tags', models.CharField(choices=[('EAT', '必吃'), ('HOTEL', '必住'), ('PLAY', '必玩'), ('VISIT', '必逛')], max_length=10)),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]