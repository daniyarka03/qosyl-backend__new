# Generated by Django 4.2.4 on 2023-08-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_post_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.CharField(blank=True, max_length=1000000, null=True),
        ),
    ]