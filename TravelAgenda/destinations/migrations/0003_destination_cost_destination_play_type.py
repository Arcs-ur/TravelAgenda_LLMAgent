# Generated by Django 5.1.1 on 2024-10-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0002_destination_image_destination_introduction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='play_type',
            field=models.CharField(blank=True, choices=[('FAMILY', '亲子路线'), ('CITYSCAPE', '城市景观'), ('NATURE', '自然景观'), ('CULTURE', '历史人文'), ('ADVENTURE', '冒险探索'), ('SPORTS', '运动休闲')], help_text='仅适用于必玩标签', max_length=15, null=True),
        ),
    ]
