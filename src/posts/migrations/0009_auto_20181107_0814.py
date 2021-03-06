# Generated by Django 2.1.1 on 2018-11-07 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20181005_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='contributor',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='briefing',
            field=models.CharField(blank=True, max_length=360, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_caption',
            field=models.CharField(blank=True, max_length=360, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
