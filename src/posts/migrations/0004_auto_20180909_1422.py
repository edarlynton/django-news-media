# Generated by Django 2.1.1 on 2018-09-09 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='caption',
        ),
    ]
