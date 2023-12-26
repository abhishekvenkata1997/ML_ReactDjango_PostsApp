# Generated by Django 5.0 on 2023-12-19 07:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_post_image_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, default='Users/abhishekvenkata/Desktop/abhishek.jpg', null=True, upload_to='store/img'),
        ),
        migrations.AlterField(
            model_name='image',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.post', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='Default content'),
        ),
    ]
